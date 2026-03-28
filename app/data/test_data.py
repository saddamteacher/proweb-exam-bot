from app.data.data_analyst_questions import DATA_ANALYST_QUESTIONS
from app.data.frontend_questions import FRONTEND_QUESTIONS
from app.data.ms_office_questions import MS_OFFICE_QUESTIONS
from app.data.python_questions import PYTHON_QUESTIONS


DEFAULT_COURSES = {
    "python": {
        "title": "Python",
        "description": "Python, Telegram Bot, Django va OOP bo‘yicha scenario formatdagi 40 ta test.",
        "questions": PYTHON_QUESTIONS[:40],
    },
    "frontend_javascript": {
        "title": "Frontend Development",
        "description": "HTML, CSS, JavaScript va React bo‘yicha 40 ta frontend testi.",
        "questions": FRONTEND_QUESTIONS[:40],
    },
    "data_analytics": {
        "title": "Data Analyst",
        "description": "Python syntax, kutubxonalar va SQL bo‘yicha 24 ta data analytics testi.",
        "questions": DATA_ANALYST_QUESTIONS,
    },
    "english": {
        "title": "MS Office",
        "description": "MS Office bo‘yicha 10 ta amaliy test.",
        "questions": MS_OFFICE_QUESTIONS,
    },
}
