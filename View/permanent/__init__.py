__all__ = ("router", )

from aiogram import Router

from .choose_permanent import router as permanent_router

router = Router()

router.include_router(permanent_router)