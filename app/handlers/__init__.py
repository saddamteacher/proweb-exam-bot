from app.handlers.admin import router as admin_router
from app.handlers.start import router as start_router
from app.handlers.tests import router as tests_router


def get_routers():
    return [start_router, tests_router, admin_router]
