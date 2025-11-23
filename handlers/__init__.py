# handlers/__init__.py
from .add_handler import add_note
from .list_handler import list_notes
from .clear_handler import clear_notes
from .delete_handler import del_note
from .edit_handler import edit_note


__all__ = [
    "add_note",
    "list_notes",
    "clear_notes",
    "del_note",
    "edit_note"
]