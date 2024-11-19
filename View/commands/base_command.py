from aiogram import Router, Bot, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, CommandObject

from config import settings
from keyboards.start_kb import star_keyboard

router = Router(name=__name__)

bot = Bot(token=settings.bot_token)

@router.message(CommandStart())
async def start_menu(message: types.Message):
    await message.answer(
        text=f"<b>Вiтаю, {message.from_user.full_name} 🌸</b> \n"
            "В цьому ботi ти зможеш переглянути моi роботи та зробити запис на послугу 👑",
        parse_mode=ParseMode.HTML,
        reply_markup=star_keyboard()
    )
