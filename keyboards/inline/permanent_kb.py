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

class EnterDateServiceActions(IntEnum):
    now = auto()
    tomorow = auto()

class EnterDateServiceDate(CallbackData, prefix = "enter_date"):
    actions = EnterDateServiceActions


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
        callback_data=EnterDateServiceDate(actions=EnterDateServiceActions.now)
    )
    builder.button(
        text = "Завтра",
        callback_data=EnterDateServiceDate(actions=EnterDateServiceActions.tomorow)
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

def enter_time():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="10:00",
        callback_data="a"
    )

    builder.button(
        text="12:00",
        callback_data="a"
    )

    builder.button(
        text="14:00",
        callback_data="a"
    )

    builder.adjust(1)

    return builder.as_markup()

def enter_pay():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="⚫️ Mono",
        callback_data="a"
    )

    builder.button(
        text="🟢 Privat",
        callback_data="a"
    )

    builder.button(
        text="💸 Готівка",
        callback_data="a"
    )

    builder.adjust(2, 1)

    return builder.as_markup()

def confirm_entry():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Підтвердити ✅",
        callback_data="A"
    )
    
    builder.button(
        text="Відмінити ❌",
        callback_data="A"
    )

    builder.adjust(1)

    return builder.as_markup()

def enter_reson_cancel():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="⏰ Змінити час запису",
        callback_data="a"
    )

    builder.button(
        text="📅  Змінити дату запису",
        callback_data="a"
    )

    builder.button(
        text="Відмінити ❌",
        callback_data="a"
    )