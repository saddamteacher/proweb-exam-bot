import asyncio
import logging
from contextlib import suppress

from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

from app.config import Settings, get_settings
from app.database.db import Database
from app.handlers import get_routers


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )


def build_bot() -> Bot:
    settings = get_settings()
    return Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )


def build_dispatcher(database: Database, settings: Settings) -> Dispatcher:
    dp = Dispatcher(storage=MemoryStorage())
    dp["db"] = database
    dp["settings"] = settings
    for router in get_routers():
        dp.include_router(router)
    return dp


async def build_database(settings: Settings) -> Database:
    database = Database(settings.db_path)
    await database.connect()
    await database.seed_defaults()
    return database


async def health_handler(_: web.Request) -> web.Response:
    return web.Response(text="ok")


async def run_polling(settings: Settings) -> None:
    database = await build_database(settings)
    bot = build_bot()
    dp = build_dispatcher(database, settings)

    try:
        await bot.delete_webhook(drop_pending_updates=False)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()
        await database.close()


async def run_webhook(settings: Settings) -> None:
    database = await build_database(settings)
    bot = build_bot()
    dp = build_dispatcher(database, settings)

    app = web.Application()
    app.router.add_get("/", health_handler)
    app.router.add_get("/health", health_handler)

    request_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        handle_in_background=True,
        secret_token=settings.webhook_secret,
    )
    request_handler.register(app, path=settings.webhook_path)
    setup_application(app, dp, bot=bot, db=database, settings=settings)

    async def on_startup(_: web.Application) -> None:
        await bot.set_webhook(
            settings.webhook_url,
            secret_token=settings.webhook_secret,
            allowed_updates=dp.resolve_used_update_types(),
            drop_pending_updates=False,
        )
        logging.info("Webhook set to %s", settings.webhook_url)

    async def on_shutdown(_: web.Application) -> None:
        with suppress(Exception):
            await bot.delete_webhook(drop_pending_updates=False)
        await database.close()

    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host="0.0.0.0", port=settings.port)
    await site.start()
    logging.info("Webhook server started on 0.0.0.0:%s", settings.port)

    try:
        await asyncio.Event().wait()
    finally:
        await runner.cleanup()


async def main() -> None:
    configure_logging()
    settings = get_settings()
    logging.info(
        "Startup mode check | webhook_enabled=%s | webhook_base_url=%r | webhook_path=%s | port=%s",
        settings.webhook_enabled,
        settings.webhook_base_url,
        settings.webhook_path,
        settings.port,
    )
    if settings.webhook_enabled:
        await run_webhook(settings)
        return
    await run_polling(settings)


if __name__ == "__main__":
    asyncio.run(main())
