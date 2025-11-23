# handlers/clear_handler.py
import sqlite3


async def clear_notes(user_id):
    with sqlite3.connect('notes.db') as db:
        cur = db.cursor()
        cur.execute('DELETE FROM notes WHERE user_id = ?', (user_id,))