# main.py
import asyncio
import logging
import sqlite3

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import settings
from routers import common_router, notes_router


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s: %(message)s',
    filename=f"logs/{__name__}.log"
)
logger = logging.getLogger(__name__)


async def main() -> None:
    logger.info("Запуск бота.")

    bot = Bot(token=settings.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()

    dp.include_router(common_router)
    dp.include_router(notes_router)

    with sqlite3.connect("notes.db") as db:
        cur = db.cursor()
        cur.execute(
            """
                CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    text TEXT NOT NULL,
                    created_at TEXT NOT NULL
                );
            """
        )

    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.exception(e)
    finally:
        logger.info("Остановка бота.")

if __name__ == '__main__':
    asyncio.run(main())