# handlers/list_handler.py
import sqlite3

from zoneinfo import ZoneInfo
from datetime import datetime


async def list_notes(user_id):
    with sqlite3.connect("notes.db") as db:
        cur = db.cursor()
        cur.execute(
            """
                SELECT text, created_at FROM notes WHERE user_id = ? ORDER BY created_at;
            """, (user_id,)
        )
        rows = cur.fetchall()

    if len(rows):
        message = "Ваши заметки:\n"
        for i, row in enumerate(rows, start=1):
            text = row[0]
            readable = datetime.fromisoformat(row[1]).astimezone(ZoneInfo("Europe/Minsk")).strftime("%d.%m.%Y %H:%M")
            message += f"<b>{i}. {text}</b> <i>(создана {readable})</i>\n"

        return message
    else:
        return "У вас нет заметок."