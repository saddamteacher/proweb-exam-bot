LANGUAGE_META = {
    "uz": {"label": "🇺🇿 UZ", "style": "success"},
    "ru": {"label": "🇷🇺 RU", "style": "primary"},
}

COURSE_LABELS = {
    "uz": {
        "python": "PYTHON",
        "frontend_javascript": "FRONTEND DEVELOPMENT",
        "data_analytics": "DATA ANALYST",
        "english": "MS OFFICE",
    },
    "ru": {
        "python": "PYTHON",
        "frontend_javascript": "FRONTEND DEVELOPMENT",
        "data_analytics": "DATA ANALYST",
        "english": "MS OFFICE",
    },
}


TRANSLATIONS = {
    "uz": {
        "choose_language": "TILNI TANLANG",
        "ask_name": "ISMINGIZNI YUBORING.",
        "ask_name_text": "ISMNI MATN KO‘RINISHIDA YUBORING.",
        "ask_contact": "TELEFON RAQAMINGIZNI KONTAKT KO‘RINISHIDA YUBORING.",
        "own_contact_only": "O‘ZINGIZNING KONTAKTINGIZNI YUBORING.",
        "contact_received": "MA’LUMOTLAR QABUL QILINDI.",
        "contact_button": "KONTAKTNI YUBORISH",
        "contact_placeholder": "TELEFON RAQAMINGIZNI YUBORING",
        "contact_retry": "KONTAKTNI PASTDAGI TUGMA ORQALI YUBORING.",
        "welcome": "SALOM {name} 👋🏻\nPROWEB EXAM BOTIGA XUSH KELIBSIZ\nTEST BOSHLASH UCHUN KERAKLI YO‘NALISHNI TANLANG.",
        "courses_title": "TEST BOSHLASH UCHUN KERAKLI YO‘NALISHNI TANLANG.",
        "select_from_buttons": "PASTDAGI TUGMALARDAN TANLANG.",
        "course_not_found": "KURS TOPILMADI.",
        "no_questions": "BU KURS UCHUN SAVOLLAR HALI QO‘SHILMAGAN.",
        "restart_label": "YANGI TEST",
        "skip_label": "SAVOLNI O‘TKAZISH",
        "finish_label": "TESTNI TUGATISH",
        "answer_prompt": "JAVOBNI TUGMALAR ORQALI TANLANG.",
        "thanks": "ISHTIROK ETGANINGIZ UCHUN RAHMAT.\nSIZGA TEZ ORADA ALOQAGA CHIQAMIZ 👋🏻",
        "question_title": "SAVOL {current}/{total}",
        "help": "BUYRUQLAR:\n/START - MENYU\n/HELP - YORDAM",
    },
    "ru": {
        "choose_language": "ВЫБЕРИТЕ ЯЗЫК",
        "ask_name": "ОТПРАВЬТЕ ВАШЕ ИМЯ.",
        "ask_name_text": "ОТПРАВЬТЕ ИМЯ В ВИДЕ ТЕКСТА.",
        "ask_contact": "ОТПРАВЬТЕ НОМЕР ТЕЛЕФОНА ЧЕРЕЗ КОНТАКТ.",
        "own_contact_only": "ОТПРАВЬТЕ СВОЙ СОБСТВЕННЫЙ КОНТАКТ.",
        "contact_received": "ДАННЫЕ ПРИНЯТЫ.",
        "contact_button": "ОТПРАВИТЬ КОНТАКТ",
        "contact_placeholder": "ОТПРАВЬТЕ НОМЕР ТЕЛЕФОНА",
        "contact_retry": "ОТПРАВЬТЕ КОНТАКТ ЧЕРЕЗ КНОПКУ НИЖЕ.",
        "welcome": "ПРИВЕТ {name} 👋🏻\nДОБРО ПОЖАЛОВАТЬ В PROWEB EXAM\nДЛЯ НАЧАЛА ТЕСТА ВЫБЕРИТЕ НУЖНОЕ НАПРАВЛЕНИЕ.",
        "courses_title": "ВЫБЕРИТЕ НУЖНОЕ НАПРАВЛЕНИЕ ДЛЯ ТЕСТА.",
        "select_from_buttons": "ВЫБЕРИТЕ ВАРИАНТ ИЗ КНОПОК НИЖЕ.",
        "course_not_found": "КУРС НЕ НАЙДЕН.",
        "no_questions": "ДЛЯ ЭТОГО КУРСА ПОКА НЕТ ВОПРОСОВ.",
        "restart_label": "НОВЫЙ ТЕСТ",
        "skip_label": "ПРОПУСТИТЬ ВОПРОС",
        "finish_label": "ЗАВЕРШИТЬ ТЕСТ",
        "answer_prompt": "ВЫБЕРИТЕ ОТВЕТ С ПОМОЩЬЮ КНОПОК.",
        "thanks": "СПАСИБО ЗА УЧАСТИЕ.\nМЫ СВЯЖЕМСЯ С ВАМИ В БЛИЖАЙШЕЕ ВРЕМЯ 👋🏻",
        "question_title": "ВОПРОС {current}/{total}",
        "help": "КОМАНДЫ:\n/START - МЕНЮ\n/HELP - ПОМОЩЬ",
    },
}


NOTIFICATION_TRANSLATIONS = {
    "uz": {
        "title": "YANGI O‘QUVCHI NATIJASI",
        "time": "VAQTI",
        "student": "O‘QUVCHI",
        "phone": "TEL RAQAMI",
        "profile": "TG USERI",
        "course": "YO‘NALISH",
        "result": "NATIJA",
        "block": "BLOK",
        "profile_link": "profil havolasi",
    },
    "ru": {
        "title": "РЕЗУЛЬТАТ НОВОГО УЧЕНИКА",
        "time": "ВРЕМЯ",
        "student": "УЧЕНИК",
        "phone": "ТЕЛЕФОН",
        "profile": "TG USER",
        "course": "НАПРАВЛЕНИЕ",
        "result": "РЕЗУЛЬТАТ",
        "block": "БЛОК",
        "profile_link": "ссылка на профиль",
    },
}


def normalize_lang(lang_code: str | None) -> str:
    if lang_code in TRANSLATIONS:
        return lang_code
    return "uz"


def t(lang_code: str | None, key: str, **kwargs: str | int) -> str:
    lang = normalize_lang(lang_code)
    template = TRANSLATIONS[lang][key]
    return template.format(**kwargs)


def course_label(lang_code: str | None, slug: str, fallback: str) -> str:
    lang = normalize_lang(lang_code)
    return COURSE_LABELS.get(lang, {}).get(slug, fallback)
