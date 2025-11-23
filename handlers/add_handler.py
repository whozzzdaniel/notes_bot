# handlers/add_handler.py
import sqlite3


async def add_note(user_id, text, created_at, message_obj):
    if text == "/add" or not text:
        await message_obj.answer("Заметка не может быть пустой.")
    else:
        with sqlite3.connect("notes.db") as db:
            cur = db.cursor()
            cur.execute(
            """
                    INSERT INTO notes (user_id, text, created_at) VALUES (?, ?, ?);
                """,(user_id, text, created_at)
            )
        await message_obj.answer("Заметка добавлена.")