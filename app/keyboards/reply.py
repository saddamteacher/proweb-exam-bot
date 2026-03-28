from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

from app.utils.i18n import LANGUAGE_META, t


def language_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=LANGUAGE_META["uz"]["label"], style=LANGUAGE_META["uz"]["style"]),
                KeyboardButton(text=LANGUAGE_META["ru"]["label"], style=LANGUAGE_META["ru"]["style"]),
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="CHOOSE LANGUAGE",
    )


def contact_keyboard(lang_code: str) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=t(lang_code, "contact_button"), request_contact=True, style="primary")]],
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder=t(lang_code, "contact_placeholder"),
    )


def remove_keyboard() -> ReplyKeyboardRemove:
    return ReplyKeyboardRemove()
