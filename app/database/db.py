import json
import sqlite3
from pathlib import Path
from typing import Any

import aiosqlite

from app.data.test_data import DEFAULT_COURSES


def _try_parse_json_text(value: str) -> Any:
    try:
        return json.loads(value)
    except (json.JSONDecodeError, TypeError):
        return value


class Database:
    def __init__(self, db_path: str) -> None:
        self.db_path = Path(db_path)
        self.connection: aiosqlite.Connection | None = None

    async def connect(self) -> None:
        self.connection = await aiosqlite.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row
        await self._create_tables()

    async def close(self) -> None:
        if self.connection:
            await self.connection.close()

    async def _create_tables(self) -> None:
        assert self.connection is not None
        await self.connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                slug TEXT UNIQUE NOT NULL,
                title TEXT NOT NULL,
                description TEXT DEFAULT ''
            );

            CREATE TABLE IF NOT EXISTS questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_id INTEGER NOT NULL,
                question_text TEXT NOT NULL,
                options_json TEXT NOT NULL,
                correct_option TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (course_id) REFERENCES courses (id) ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                full_name TEXT NOT NULL,
                username TEXT,
                course_id INTEGER NOT NULL,
                correct_answers INTEGER NOT NULL,
                wrong_answers INTEGER NOT NULL,
                percentage REAL NOT NULL,
                level_title TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (course_id) REFERENCES courses (id) ON DELETE CASCADE
            );
            """
        )
        await self.connection.commit()

    async def seed_defaults(self) -> None:
        for slug, course in DEFAULT_COURSES.items():
            existing = await self.get_course_by_slug(slug)
            if existing:
                course_id = existing["id"]
                await self.connection.execute(
                    "UPDATE courses SET title = ?, description = ? WHERE id = ?",
                    (course["title"], course["description"], course_id),
                )
                await self.clear_questions_by_course(course_id)
            else:
                course_id = await self.add_course(slug, course["title"], course["description"])
            for question in course["questions"]:
                await self.add_question(
                    course_id=course_id,
                    question_text=question["question"],
                    options=question["options"],
                    correct_option=question["correct"],
                )
        await self.connection.commit()

    async def add_course(self, slug: str, title: str, description: str = "") -> int:
        assert self.connection is not None
        cursor = await self.connection.execute(
            """
            INSERT INTO courses (slug, title, description)
            VALUES (?, ?, ?)
            """,
            (slug, title, description),
        )
        await self.connection.commit()
        return int(cursor.lastrowid)

    async def get_courses(self) -> list[dict[str, Any]]:
        assert self.connection is not None
        cursor = await self.connection.execute(
            "SELECT id, slug, title, description FROM courses ORDER BY id"
        )
        rows = await cursor.fetchall()
        return [dict(row) for row in rows]

    async def get_course_by_slug(self, slug: str) -> dict[str, Any] | None:
        assert self.connection is not None
        cursor = await self.connection.execute(
            "SELECT id, slug, title, description FROM courses WHERE slug = ?",
            (slug,),
        )
        row = await cursor.fetchone()
        return dict(row) if row else None

    async def get_course_by_id(self, course_id: int) -> dict[str, Any] | None:
        assert self.connection is not None
        cursor = await self.connection.execute(
            "SELECT id, slug, title, description FROM courses WHERE id = ?",
            (course_id,),
        )
        row = await cursor.fetchone()
        return dict(row) if row else None

    async def add_question(
        self,
        course_id: int,
        question_text: str | dict[str, str],
        options: dict[str, str] | dict[str, dict[str, str]],
        correct_option: str,
    ) -> int:
        assert self.connection is not None
        cursor = await self.connection.execute(
            """
            INSERT INTO questions (course_id, question_text, options_json, correct_option)
            VALUES (?, ?, ?, ?)
            """,
            (
                course_id,
                json.dumps(question_text, ensure_ascii=False) if isinstance(question_text, dict) else question_text,
                json.dumps(options, ensure_ascii=False),
                correct_option,
            ),
        )
        await self.connection.commit()
        return int(cursor.lastrowid)

    async def clear_questions_by_course(self, course_id: int) -> None:
        assert self.connection is not None
        await self.connection.execute("DELETE FROM questions WHERE course_id = ?", (course_id,))
        await self.connection.commit()

    async def get_questions_by_course(self, course_id: int) -> list[dict[str, Any]]:
        assert self.connection is not None
        cursor = await self.connection.execute(
            """
            SELECT id, question_text, options_json, correct_option
            FROM questions
            WHERE course_id = ?
            ORDER BY id
            """,
            (course_id,),
        )
        rows = await cursor.fetchall()
        questions = []
        for row in rows:
            item = dict(row)
            item["question_text"] = _try_parse_json_text(item["question_text"])
            item["options"] = json.loads(item.pop("options_json"))
            questions.append(item)
        return questions

    async def save_result(
        self,
        user_id: int,
        full_name: str,
        username: str | None,
        course_id: int,
        correct_answers: int,
        wrong_answers: int,
        percentage: float,
        level_title: str,
    ) -> None:
        assert self.connection is not None
        await self.connection.execute(
            """
            INSERT INTO results (
                user_id, full_name, username, course_id, correct_answers,
                wrong_answers, percentage, level_title
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                user_id,
                full_name,
                username,
                course_id,
                correct_answers,
                wrong_answers,
                percentage,
                level_title,
            ),
        )
        await self.connection.commit()

    async def get_statistics(self) -> dict[str, Any]:
        assert self.connection is not None
        cursor = await self.connection.execute(
            """
            SELECT
                COUNT(*) AS total_attempts,
                COUNT(DISTINCT user_id) AS unique_users,
                COALESCE(ROUND(AVG(percentage), 2), 0) AS average_percentage
            FROM results
            """
        )
        overview = dict(await cursor.fetchone())

        course_cursor = await self.connection.execute(
            """
            SELECT c.title, COUNT(r.id) AS attempts, COALESCE(ROUND(AVG(r.percentage), 2), 0) AS avg_score
            FROM courses c
            LEFT JOIN results r ON r.course_id = c.id
            GROUP BY c.id
            ORDER BY c.id
            """
        )
        overview["courses"] = [dict(row) for row in await course_cursor.fetchall()]
        return overview
