__all__ = ("router", )

from aiogram import Router

from .commands import router as commands_router
from .reply_start_heandlers import router as reply_star_router

router = Router(name=__name__)

router.include_routers(
    commands_router,
    reply_star_router
    )