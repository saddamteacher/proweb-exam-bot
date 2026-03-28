from aiogram.fsm.state import State, StatesGroup


class UserOnboarding(StatesGroup):
    waiting_language = State()
    waiting_name = State()
    waiting_contact = State()
    menu = State()


class TestSession(StatesGroup):
    in_progress = State()


class AdminPanel(StatesGroup):
    waiting_course = State()
    waiting_question = State()
