import asyncio
import logging
from aiogram import Bot, F
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import CommandStart, Command, CommandObject #обработчик команды старт и команд
from aiogram.utils import markdown
from aiogram.enums import ParseMode, ChatAction
from aiogram.utils.chat_action import ChatActionSender

from config import settings
from View.commands.base_command import router
from View import router as main_router


bot = Bot(token=settings.bot_token)
dp = Dispatcher()

dp.include_router(main_router)

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(
        token = settings.bot_token
        )
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())