from aiogram import Router, Bot, types

from config import settings
from keyboards.inline.permanent_kb import permanent_keyboard

router = Router(name=__name__)

bot = Bot(token=settings.bot_token)

@router.message()
async def choose_permanent_menu(message: types.Message):
    await message.edit_text(
        text="Оберіть послугу перманентного макіяжу",
        reply_markup=permanent_keyboard()
    )