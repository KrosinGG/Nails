from aiogram.utils.keyboard import InlineKeyboardBuilder
from enum import IntEnum, auto
from aiogram.filters.callback_data import CallbackData
from typing import Optional

class PermanentActions(IntEnum):
    lips = auto() 
    brows = auto() 
    lashes = auto() 

class PermanentData(CallbackData, prefix = "permanent"):
    actions: PermanentActions
    value: Optional[str] = None

def permanent_keyboard():
    builder = InlineKeyboardBuilder()

    builder.button(text="🫦 Перманент губ", callback_data=PermanentData(actions=PermanentActions.lips, value="permanen"))
    builder.button(text="😻 Перманент брів", callback_data=PermanentData(actions=PermanentActions.brows, value="permanen"))
    builder.button(text="👑 Міжвійковий перманент", callback_data=PermanentData(actions=PermanentActions.lashes, value="permanen"))

    builder.adjust(1)

    return builder.as_markup()

def enter_date():
    builder = InlineKeyboardBuilder()

    builder.button(
        text = "Сьогодні",
        callback_data="a"
    )
    builder.button(
        text = "Завтра",
        callback_data="a"
    )
    builder.button(
        text = "date +1",
        callback_data="a"
    )
    builder.button(
        text = "date +2",
        callback_data="a"
    )
    builder.button(
        text = "date +3",
        callback_data="a"
    )

    builder.adjust(2,3)

    return builder.as_markup()