from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from app.utils.i18n import course_label, normalize_lang, t

COURSE_META = {
    "python": {"style": "success"},
    "frontend_javascript": {"style": "primary"},
    "data_analytics": {"style": "danger"},
    "english": {"style": "success"},
}

COURSE_COLOR_HINT = {
    "python": "",
    "frontend_javascript": "",
    "data_analytics": "",
    "english": "",
}

ANSWER_META = {
    "A": {"style": "success"},
    "B": {"style": "primary"},
    "C": {"style": "danger"},
    "D": {"style": "success"},
}

def _button(text: str, style: str) -> KeyboardButton:
    return KeyboardButton(text=text, style=style)


def course_button_text(course: dict, lang_code: str) -> str:
    return course_label(lang_code, course["slug"], course["title"]).upper()


def course_slug_by_text(courses: list[dict], text: str) -> str | None:
    for course in courses:
        if course_button_text(course, "uz") == text or course_button_text(course, "ru") == text:
            return course["slug"]
    return None


def courses_keyboard(courses: list[dict], lang_code: str) -> ReplyKeyboardMarkup:
    buttons = []
    current_row = []
    for course in courses:
        meta = COURSE_META.get(course["slug"], {"style": "primary"})
        current_row.append(_button(course_button_text(course, lang_code), meta["style"]))
        if len(current_row) == 2:
            buttons.append(current_row)
            current_row = []
    if current_row:
        buttons.append(current_row)
    return ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        input_field_placeholder=t(lang_code, "courses_title"),
    )


def resolve_option_text(option_value: str | dict, lang_code: str) -> str:
    if isinstance(option_value, dict):
        lang = normalize_lang(lang_code)
        return str(option_value.get(lang) or option_value.get("uz") or next(iter(option_value.values()), ""))
    return str(option_value)


def answer_button_text(option_key: str, option_value: str | dict, lang_code: str) -> str:
    return resolve_option_text(option_value, lang_code).upper()


def answer_key_by_text(options: dict[str, str | dict], text: str, lang_code: str) -> str | None:
    for key, value in options.items():
        if answer_button_text(key, value, lang_code) == text:
            return key
    return None


def answer_keyboard(course_slug: str, options: dict[str, str | dict], lang_code: str) -> ReplyKeyboardMarkup:
    style = COURSE_META.get(course_slug, {"style": "primary"})["style"]
    action_style = "primary" if course_slug == "data_analytics" else "danger"
    rows = []
    current_row = []
    for key, value in options.items():
        current_row.append(_button(answer_button_text(key, value, lang_code), style))
        if len(current_row) == 2:
            rows.append(current_row)
            current_row = []
    if current_row:
        rows.append(current_row)
    rows.append(
        [
            _button(t(lang_code, "skip_label"), action_style),
            _button(t(lang_code, "finish_label"), action_style),
        ]
    )
    return ReplyKeyboardMarkup(
        keyboard=rows,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder=t(lang_code, "answer_prompt"),
    )


def result_keyboard(lang_code: str) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[_button(t(lang_code, "restart_label"), "success")]],
        resize_keyboard=True,
        input_field_placeholder=t(lang_code, "restart_label"),
    )


def admin_panel_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [_button("KURS QO‘SHISH", "success"), _button("SAVOL QO‘SHISH", "primary")],
            [_button("STATISTIKA", "primary"), _button("MENYU", "danger")],
        ],
        resize_keyboard=True,
        input_field_placeholder="ADMIN BO‘LIMINI TANLANG",
    )


def admin_courses_keyboard(courses: list[dict]) -> ReplyKeyboardMarkup:
    buttons = []
    current_row = []
    for course in courses:
        meta = COURSE_META.get(course["slug"], {"style": "primary"})
        current_row.append(_button(course_button_text(course, "uz"), meta["style"]))
        if len(current_row) == 2:
            buttons.append(current_row)
            current_row = []
    if current_row:
        buttons.append(current_row)
    buttons.append([_button("ADMIN MENYU", "danger")])
    return ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        input_field_placeholder="KURSNI TANLANG",
    )
