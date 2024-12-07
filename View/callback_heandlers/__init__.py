from aiogram import Router

from .permanent_heandlers import router as permanent_heandlers_router

router = Router(name=__name__)

router.include_routers(
    permanent_heandlers_router
)