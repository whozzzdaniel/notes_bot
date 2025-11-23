# routers/notes.py
import logging

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from handlers import list_notes, add_note, clear_notes, del_note, edit_note


logger = logging.getLogger(__name__)
router = Router()

@router.message(Command("add"))
async def cmd_add(message: Message):
    logger.info("Команда add")

    try:
        await add_note(
            user_id = message.from_user.id,
            text = message.text.split(" ", 1)[-1],
            created_at = message.date.isoformat(),
            message_obj = message
        )
    except Exception as e:
        logger.error(e)

        await message.answer("Не удалось добавить заметку.")


@router.message(Command("del"))
async def cmd_del(message: Message):
    logger.info("Команда del")

    try:
        note_pos = int(message.text.split(" ", 1)[-1])
        await del_note(message.from_user.id, note_pos, message)
    except Exception as e:
        logger.error(e)

        await message.answer("Введено неверное значение.")


@router.message(Command("clear"))
async def cmd_clear(message: Message):
    logger.info("Команда clear")

    await clear_notes(message.from_user.id)
    await message.answer("Заметки очищены")


@router.message(Command("list"))
async def cmd_list(message: Message):
    logger.info("Команда list")

    try:
        await list_notes(message.from_user.id, message)
    except Exception as e:
        logger.error(e)

        await message.answer("Произошла ошибка.")

@router.message(Command("edit"))
async def cmd_edit(message: Message):
    logger.info("Команда edit")

    try:
        note_pos = int(message.text.split(" ", 2)[-2])
        text = message.text.split(" ", 2)[-1]
        await edit_note(message.from_user.id, note_pos, text, message)
    except Exception as e:
        logger.error(e)

        await message.answer("Введено неверное значение.")