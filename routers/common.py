# routers/common.py
import logging

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


logger = logging.getLogger(__name__)
router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    logger.info("Команда start")
    await message.answer(
"""Привет! Это бот, который помогает хранить твои заметки.\n
Напиши /help, чтобы просмотреть список команд."""
    )

@router.message(Command("help"))
async def cmd_help(message: Message):
    logger.info("Команда help")
    await message.answer(
"""Список команд:\n
/add (текст заметки) – добавить новую заметку\n
/del (номер заметки в списке) – удалить заметку по номеру\n
/clear – очистить весь список\n
/list – просмотреть список заметок\n
/edit (номер заметки в списке, текст заметки) – отредактировать заметку по номеру\n"""
    )