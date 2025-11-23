# routers/__init__.py
from .common import router as common_router
from .notes import router as notes_router


__all__ = [
    "common_router",
    "notes_router"
]