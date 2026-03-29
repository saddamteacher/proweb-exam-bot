import logging
from datetime import datetime

from aiogram import Bot

from app.config import Settings
from app.utils.i18n import NOTIFICATION_TRANSLATIONS, normalize_lang


logger = logging.getLogger(__name__)


def build_profile_reference(user_id: int, username: str | None, lang_code: str) -> str:
    if username:
        return f"@{username}"
    return f'<a href="tg://user?id={user_id}">{NOTIFICATION_TRANSLATIONS[lang_code]["profile_link"]}</a>'


def calculate_block(correct_answers: int, total_questions: int) -> str:
    if total_questions <= 0:
        return "0"
    if total_questions <= 10:
        percentage = (correct_answers / total_questions) * 100
        return "1" if percentage >= 70 else "0"
    total_blocks = max(1, total_questions // 8)
    passed_blocks = correct_answers // 8
    if passed_blocks == 0:
        return "0"
    return str(min(total_blocks, passed_blocks + 1))


async def send_result_notification(
    bot: Bot,
    settings: Settings,
    *,
    student_name: str,
    phone_number: str,
    user_id: int,
    username: str | None,
    lang_code: str,
    course_title: str,
    percentage: float,
    correct_answers: int,
    total_questions: int,
    answer_history: list[dict[str, int | str]],
) -> None:
    if not settings.results_chat_id:
        return
    lang = normalize_lang(lang_code)
    tr = NOTIFICATION_TRANSLATIONS[lang]
    flag = "🇺🇿" if lang == "uz" else "🇷🇺"
    timestamp = datetime.now(settings.timezone).strftime("%H:%M %d/%m/%Y")

    text = (
        f"<b>{tr['title']}</b>\n\n"
        f"{tr['time']}: <b>{timestamp}</b>\n"
        f"{tr['student']}: <b>{student_name}</b>\n"
        f"{tr['phone']}: <b>{phone_number}</b>\n"
        f"{tr['profile']}: {build_profile_reference(user_id, username, lang)}\n"
        f"{tr['course']}: <b>{flag} {course_title}</b>\n"
        f"{tr['result']}: <b>{correct_answers}/{total_questions}</b> ({percentage}%)\n"
        f"{tr['block']}: <b>{calculate_block(correct_answers, total_questions)}</b>"
    )
    try:
        await bot.send_message(chat_id=settings.results_chat_id, text=text)
    except Exception:
        logger.exception("Failed to send result notification")
