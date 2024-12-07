from aiogram import Router, Bot, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, CommandObject

from config import settings
from db_manager import init_db, add_user, get_user_chat_id
from keyboards.start_kb import star_keyboard

router = Router(name=__name__)

bot = Bot(token=settings.bot_token)

# Инициализация базы при запуске
init_db()

@router.message(CommandStart())
async def start_menu(message: types.Message):
    chat_id = message.from_user.id
    user = get_user_chat_id(chat_id)

    if not user:
        add_user(
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
            chat_id
                )

    await message.answer(
        text=f"<b>Вiтаю, {message.from_user.full_name} 🌸</b> \n"
            "В цьому ботi ти зможеш переглянути моi роботи та зробити запис на послугу 👑",
        parse_mode=ParseMode.HTML,
        reply_markup=star_keyboard()
    )
