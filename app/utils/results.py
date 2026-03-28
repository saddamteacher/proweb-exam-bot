import re
from html import escape

from app.utils.i18n import normalize_lang, t


def calculate_level(percentage: float) -> str:
    if percentage >= 90:
        return "EXPERT"
    if percentage >= 70:
        return "GOOD"
    if percentage >= 50:
        return "BEGINNER"
    return "LEARN MORE"


def resolve_localized_text(value: str | dict, lang_code: str) -> str:
    if isinstance(value, dict):
        lang = normalize_lang(lang_code)
        return str(value.get(lang) or value.get("uz") or next(iter(value.values()), ""))
    return str(value)


def render_question_text(raw_text: str | dict, lang_code: str) -> str:
    raw_value = resolve_localized_text(raw_text, lang_code)
    normalized = re.sub(r"</?pre>", "", raw_value, flags=re.DOTALL)
    normalized = re.sub(r"</?code>", "", normalized, flags=re.DOTALL)
    return f"<pre><code>{escape(normalized)}</code></pre>"


def build_timer_bar(seconds_left: int, total_seconds: int = 15, width: int = 10) -> str:
    filled = max(0, min(total_seconds, seconds_left))
    empty = max(0, total_seconds - filled)
    if seconds_left > 10:
        unit = "🟢"
    elif seconds_left > 5:
        unit = "🟡"
    elif seconds_left > 0:
        unit = "🔴"
    else:
        unit = "⚫"
    return unit * filled + "⚫" * empty


def format_question_with_timer(
    course_title: str,
    current_number: int,
    total_questions: int,
    question: dict,
    lang_code: str,
    seconds_left: int,
) -> str:
    return (
        f"{format_question_text(course_title, current_number, total_questions, question, lang_code)}\n\n"
        f"{build_timer_bar(seconds_left)}"
    )


def format_question_text(
    course_title: str, current_number: int, total_questions: int, question: dict, lang_code: str
) -> str:
    raw = render_question_text(question["question_text"], lang_code)
    prefix = f"{current_number}/{total_questions}\n\n"
    return raw.replace("<pre><code>", f"<pre><code>{prefix}", 1)


def format_result_text(
    course_title: str,
    correct_answers: int,
    wrong_answers: int,
    percentage: float,
    level_title: str,
) -> str:
    return (
        f"{course_title.upper()} TESTI YAKUNLANDI\n\n"
        f"TO‘G‘RI JAVOBLAR: {correct_answers}\n"
        f"NOTO‘G‘RI JAVOBLAR: {wrong_answers}\n"
        f"NATIJA: {percentage}%\n"
        f"LEVEL: {level_title}"
    )
