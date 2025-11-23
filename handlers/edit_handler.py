# handlers/edit_handler.py
import sqlite3


async def edit_note(user_id, note_pos, text, message_obj):
    with sqlite3.connect('notes.db') as db:
        cur = db.cursor()
        cur.execute(
            """
            SELECT id
            FROM notes
            WHERE user_id = ?
            ORDER BY id
            LIMIT 1 OFFSET ?
            """, (user_id, int(note_pos) - 1)
        )

        note_id = cur.fetchone()
        if note_id is None:
            await message_obj.answer(f"Заметка по номеру <b>{note_pos}</b> не найдена.")
        else:
            cur.execute(
                """
                UPDATE notes
                SET text = ?
                WHERE id = ? AND user_id = ?
                """, (text, note_id[0], user_id)
            )
            await message_obj.answer("Заметка изменена.")