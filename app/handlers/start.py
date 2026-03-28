from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Contact, Message

from app.database.db import Database
from app.keyboards.inline import courses_keyboard
from app.keyboards.reply import contact_keyboard, language_keyboard, remove_keyboard
from app.states.test_states import UserOnboarding
from app.utils.i18n import LANGUAGE_META, normalize_lang, t

router = Router()


def selected_lang_from_text(text: str | None) -> str | None:
    if not text:
        return None
    for code, meta in LANGUAGE_META.items():
        if text.strip() == meta["label"]:
            return code
    return None


async def show_courses(message: Message, db: Database, student_name: str, lang_code: str) -> None:
    courses = await db.get_courses()
    await message.answer(
        t(lang_code, "welcome", name=student_name),
        reply_markup=courses_keyboard(courses, lang_code),
    )


@router.message(CommandStart())
async def start_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(UserOnboarding.waiting_language)
    await message.answer(
        t("uz", "choose_language"),
        reply_markup=language_keyboard(),
    )


@router.message(UserOnboarding.waiting_language)
async def language_selected(message: Message, state: FSMContext, db: Database) -> None:
    lang_code = selected_lang_from_text(message.text)
    if not lang_code:
        await message.answer(t("uz", "choose_language"), reply_markup=language_keyboard())
        return

    await state.update_data(lang_code=lang_code)
    data = await state.get_data()
    if data.get("student_name") and data.get("phone_number"):
        await state.set_state(UserOnboarding.menu)
        await show_courses(message, db, data["student_name"], lang_code)
        return

    await state.set_state(UserOnboarding.waiting_name)
    await message.answer(t(lang_code, "ask_name"), reply_markup=remove_keyboard())


@router.message(UserOnboarding.waiting_name)
async def get_name(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    lang_code = normalize_lang(data.get("lang_code"))
    if not message.text:
        await message.answer(t(lang_code, "ask_name_text"))
        return

    student_name = message.text.strip()
    await state.update_data(student_name=student_name)
    await state.set_state(UserOnboarding.waiting_contact)
    await message.answer(
        t(lang_code, "ask_contact"),
        reply_markup=contact_keyboard(lang_code),
    )


@router.message(UserOnboarding.waiting_contact, F.contact)
async def get_contact(message: Message, state: FSMContext, db: Database) -> None:
    data = await state.get_data()
    lang_code = normalize_lang(data.get("lang_code"))
    contact: Contact = message.contact
    if contact.user_id and contact.user_id != message.from_user.id:
        await message.answer(
            t(lang_code, "own_contact_only"),
            reply_markup=contact_keyboard(lang_code),
        )
        return

    phone_number = contact.phone_number
    if not phone_number.startswith("+"):
        phone_number = f"+{phone_number}"

    await state.update_data(phone_number=phone_number)
    await state.set_state(UserOnboarding.menu)
    data = await state.get_data()

    await message.answer(t(lang_code, "contact_received"), reply_markup=remove_keyboard())
    await show_courses(message, db, data["student_name"], lang_code)


@router.message(UserOnboarding.waiting_contact)
async def reject_non_contact(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    lang_code = normalize_lang(data.get("lang_code"))
    await message.answer(
        t(lang_code, "contact_retry"),
        reply_markup=contact_keyboard(lang_code),
    )


@router.message(F.text == "/help")
async def help_handler(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    lang_code = normalize_lang(data.get("lang_code"))
    await message.answer(t(lang_code, "help"))
