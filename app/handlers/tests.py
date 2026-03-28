import asyncio
from contextlib import suppress

from aiogram import Bot, F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.config import Settings
from app.database.db import Database
from app.keyboards.inline import (
    answer_key_by_text,
    answer_keyboard,
    course_slug_by_text,
    courses_keyboard,
    result_keyboard,
)
from app.keyboards.reply import language_keyboard
from app.states.test_states import TestSession, UserOnboarding
from app.utils.i18n import course_label, normalize_lang, t
from app.utils.notifications import send_result_notification
from app.utils.results import build_timer_bar, calculate_level, format_question_with_timer

router = Router()

QUESTION_TIME_LIMIT = 15
QUESTION_TIMERS: dict[int, asyncio.Task] = {}


def cancel_question_timer(user_id: int, exclude_task: asyncio.Task | None = None) -> None:
    task = QUESTION_TIMERS.pop(user_id, None)
    if task and task is not exclude_task:
        task.cancel()
    elif task is exclude_task:
        QUESTION_TIMERS[user_id] = task


async def send_question(
    bot: Bot,
    chat_id: int,
    user_id: int,
    state: FSMContext,
    data: dict,
    db: Database,
    settings: Settings,
) -> None:
    cancel_question_timer(user_id, exclude_task=asyncio.current_task())
    questions = data["questions"]
    current_index = data["current_index"]
    question = questions[current_index]
    lang_code = normalize_lang(data.get("lang_code"))
    text = format_question_with_timer(
        data["course_title"],
        current_index + 1,
        len(questions),
        question,
        lang_code,
        QUESTION_TIME_LIMIT,
    )
    sent = await bot.send_message(
        chat_id,
        format_question_with_timer(
            data["course_title"],
            current_index + 1,
            len(questions),
            question,
            lang_code,
            QUESTION_TIME_LIMIT,
        ).rsplit("\n\n", 1)[0],
        reply_markup=answer_keyboard(data["course_slug"], question["options"], lang_code),
    )
    timer_message = await bot.send_message(chat_id, build_timer_bar(QUESTION_TIME_LIMIT, QUESTION_TIME_LIMIT))
    await state.update_data(
        question_message_id=sent.message_id,
        question_chat_id=sent.chat.id,
        question_serial=current_index,
        timer_message_id=timer_message.message_id,
    )
    QUESTION_TIMERS[user_id] = asyncio.create_task(
        question_timer(
            bot=bot,
            state=state,
            user_id=user_id,
            db=db,
            settings=settings,
            full_name=data.get("telegram_full_name"),
            username=data.get("telegram_username"),
            timer_context=await state.get_data(),
        )
    )


async def question_timer(
    bot: Bot,
    state: FSMContext,
    user_id: int,
    db: Database,
    settings: Settings,
    full_name: str | None,
    username: str | None,
    timer_context: dict,
) -> None:
    current_task = asyncio.current_task()
    question_index = timer_context["current_index"]
    chat_id = timer_context["question_chat_id"]
    message_id = timer_context["timer_message_id"]
    try:
        for seconds_left in range(QUESTION_TIME_LIMIT - 1, 0, -1):
            await asyncio.sleep(1)
            data = await state.get_data()
            if data.get("current_index") != question_index or data.get("timer_message_id") != message_id:
                return
            text = build_timer_bar(seconds_left, QUESTION_TIME_LIMIT)
            with suppress(Exception):
                await bot.edit_message_text(text=text, chat_id=chat_id, message_id=message_id)

        data = await state.get_data()
        if data.get("current_index") != question_index or data.get("timer_message_id") != message_id:
            return
        history = list(data.get("answer_history", []))
        history.append({"number": question_index + 1, "status": "timeout"})
        await state.update_data(wrong_answers=data["wrong_answers"] + 1, answer_history=history)
        await advance_to_next_question_or_finish(
            bot=bot,
            state=state,
            user_id=user_id,
            chat_id=chat_id,
            data=await state.get_data(),
            expired=True,
            db=db,
            settings=settings,
            full_name=full_name,
            username=username,
        )
    except asyncio.CancelledError:
        raise
    finally:
        if QUESTION_TIMERS.get(user_id) is current_task:
            QUESTION_TIMERS.pop(user_id, None)


async def finish_test(
    bot: Bot,
    chat_id: int,
    state: FSMContext,
    db: Database,
    settings: Settings,
    user_id: int,
    full_name: str,
    username: str | None,
    data: dict,
) -> None:
    cancel_question_timer(user_id)
    percentage = round((data["correct_answers"] / len(data["questions"])) * 100, 2)
    level_title = calculate_level(percentage)
    lang_code = normalize_lang(data.get("lang_code"))

    await db.save_result(
        user_id=user_id,
        full_name=data.get("student_name", full_name),
        username=username,
        course_id=data["course_id"],
        correct_answers=data["correct_answers"],
        wrong_answers=data["wrong_answers"],
        percentage=percentage,
        level_title=level_title,
    )
    await send_result_notification(
        bot,
        settings,
        student_name=data.get("student_name", full_name),
        phone_number=data.get("phone_number", "Noma’lum"),
        user_id=user_id,
        username=username,
        lang_code=lang_code,
        course_title=data["course_title"],
        percentage=percentage,
        correct_answers=data["correct_answers"],
        total_questions=len(data["questions"]),
        answer_history=data.get("answer_history", []),
    )
    await state.set_state(UserOnboarding.menu)
    with suppress(Exception):
        if data.get("question_message_id"):
            await bot.delete_message(chat_id, data["question_message_id"])
    with suppress(Exception):
        if data.get("timer_message_id"):
            await bot.delete_message(chat_id, data["timer_message_id"])
    await bot.send_message(
        chat_id,
        t(lang_code, "thanks"),
        reply_markup=result_keyboard(lang_code),
    )


async def advance_to_next_question_or_finish(
    *,
    bot: Bot,
    state: FSMContext,
    user_id: int,
    chat_id: int,
    data: dict,
    expired: bool = False,
    db: Database | None = None,
    settings: Settings | None = None,
    full_name: str | None = None,
    username: str | None = None,
) -> None:
    next_index = data["current_index"] + 1
    if next_index < len(data["questions"]):
        with suppress(Exception):
            if data.get("question_message_id"):
                await bot.delete_message(chat_id, data["question_message_id"])
        with suppress(Exception):
            if data.get("timer_message_id"):
                await bot.delete_message(chat_id, data["timer_message_id"])
        await state.update_data(current_index=next_index)
        next_data = await state.get_data()
        await send_question(bot, chat_id, user_id, state, next_data, db, settings)
        return

    if db is None or settings is None or full_name is None:
        return
    await finish_test(
        bot=bot,
        chat_id=chat_id,
        state=state,
        db=db,
        settings=settings,
        user_id=user_id,
        full_name=full_name,
        username=username,
        data=data,
    )


@router.message(UserOnboarding.menu)
async def course_selected(message: Message, state: FSMContext, db: Database, settings: Settings) -> None:
    if not message.text:
        return
    if message.text.startswith("/"):
        return

    data = await state.get_data()
    lang_code = normalize_lang(data.get("lang_code"))
    if not data.get("student_name") or not data.get("phone_number"):
        await state.set_state(UserOnboarding.waiting_language)
        await message.answer(t(lang_code, "choose_language"), reply_markup=language_keyboard())
        return

    courses = await db.get_courses()
    if message.text.strip() == t(lang_code, "restart_label"):
        await message.answer(
            t(lang_code, "courses_title"),
            reply_markup=courses_keyboard(courses, lang_code),
        )
        return

    slug = course_slug_by_text(courses, message.text.strip())
    if not slug:
        await message.answer(
            t(lang_code, "select_from_buttons"),
            reply_markup=courses_keyboard(courses, lang_code),
        )
        return

    course = await db.get_course_by_slug(slug)
    if not course:
        await message.answer(t(lang_code, "course_not_found"))
        return

    questions = await db.get_questions_by_course(course["id"])
    if not questions:
        await message.answer(t(lang_code, "no_questions"))
        return

    await state.set_state(TestSession.in_progress)
    await state.update_data(
        course_id=course["id"],
        course_slug=course["slug"],
        course_title=course_label(lang_code, course["slug"], course["title"]),
        questions=questions,
        current_index=0,
        correct_answers=0,
        wrong_answers=0,
        answer_history=[],
        telegram_full_name=message.from_user.full_name,
        telegram_username=message.from_user.username,
    )
    await send_question(
        message.bot,
        message.chat.id,
        message.from_user.id,
        state,
        await state.get_data(),
        db,
        settings,
    )


@router.message(TestSession.in_progress)
async def answer_selected(
    message: Message,
    state: FSMContext,
    db: Database,
    bot: Bot,
    settings: Settings,
) -> None:
    if not message.text:
        data = await state.get_data()
        await message.answer(t(data.get("lang_code"), "answer_prompt"))
        return

    data = await state.get_data()
    lang_code = normalize_lang(data.get("lang_code"))
    question = data["questions"][data["current_index"]]
    selected_text = message.text.strip()

    with suppress(Exception):
        await message.delete()

    if selected_text == t(lang_code, "finish_label"):
        cancel_question_timer(message.from_user.id)
        current_number = data["current_index"] + 1
        history = list(data.get("answer_history", []))
        answered_numbers = {int(item["number"]) for item in history}
        if current_number not in answered_numbers:
            history.append({"number": current_number, "status": "unanswered"})
        for number in range(current_number + 1, len(data["questions"]) + 1):
            if number not in answered_numbers:
                history.append({"number": number, "status": "unanswered"})
        await state.update_data(answer_history=history)
        await finish_test(
            bot=bot,
            chat_id=message.chat.id,
            state=state,
            db=db,
            settings=settings,
            user_id=message.from_user.id,
            full_name=message.from_user.full_name,
            username=message.from_user.username,
            data=await state.get_data(),
        )
        return

    if selected_text == t(lang_code, "skip_label"):
        cancel_question_timer(message.from_user.id)
        history = list(data.get("answer_history", []))
        history.append({"number": data["current_index"] + 1, "status": "skipped"})
        await state.update_data(wrong_answers=data["wrong_answers"] + 1, answer_history=history)
        await advance_to_next_question_or_finish(
            bot=bot,
            state=state,
            user_id=message.from_user.id,
            chat_id=message.chat.id,
            data=await state.get_data(),
            db=db,
            settings=settings,
            full_name=message.from_user.full_name,
            username=message.from_user.username,
        )
        return

    selected_option = answer_key_by_text(question["options"], selected_text, lang_code)
    if not selected_option:
        await message.answer(
            t(lang_code, "answer_prompt"),
            reply_markup=answer_keyboard(data["course_slug"], question["options"], lang_code),
        )
        return

    cancel_question_timer(message.from_user.id)
    history = list(data.get("answer_history", []))
    if selected_option == question["correct_option"]:
        history.append({"number": data["current_index"] + 1, "status": "correct"})
        await state.update_data(correct_answers=data["correct_answers"] + 1, answer_history=history)
    else:
        history.append({"number": data["current_index"] + 1, "status": "wrong"})
        await state.update_data(wrong_answers=data["wrong_answers"] + 1, answer_history=history)

    await advance_to_next_question_or_finish(
        bot=bot,
        state=state,
        user_id=message.from_user.id,
        chat_id=message.chat.id,
        data=await state.get_data(),
        db=db,
        settings=settings,
        full_name=message.from_user.full_name,
        username=message.from_user.username,
    )
