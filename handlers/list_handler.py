# handlers/list_handler.py
import sqlite3

from zoneinfo import ZoneInfo
from datetime import datetime


async def list_notes(user_id, message_obj):
    with sqlite3.connect("notes.db") as db:
        cur = db.cursor()
        cur.execute(
            """
                SELECT text, created_at FROM notes WHERE user_id = ? ORDER BY created_at;
            """, (user_id,)
        )
        rows = cur.fetchall()

    if len(rows):
        messages = ["Ваши заметки:\n"]
        for i, row in enumerate(rows, start=1):
            text = row[0]
            readable = datetime.fromisoformat(row[1]).astimezone(ZoneInfo("Europe/Minsk")).strftime("%d.%m.%Y %H:%M")
            messages.append(f"<b>{i}. {text}</b> <i>(создана {readable})</i>\n")

        batch = 11
        print(messages)
        for i in range(0, len(messages), batch):
            messages_batch = messages[i:i + batch]
            await message_obj.answer("".join(messages_batch))
    else:
        await message_obj.answer("У вас нет заметок.")