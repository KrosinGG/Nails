from aiogram.utils.keyboard import InlineKeyboardBuilder
from enum import IntEnum, auto
from aiogram.filters.callback_data import CallbackData

class ChooseServiceActions(IntEnum):
    nails = auto()
    pedicure = auto()
    permanent = auto()

class ChooseServiceData(CallbackData, prefix="choose_service"):
    actions: ChooseServiceActions

def servise_inline():
    builder = InlineKeyboardBuilder()

    builder.button(text="💅🏼 Маникюр",callback_data=ChooseServiceData(actions=ChooseServiceActions.nails))
    builder.button(text="👣 Педикюр",callback_data=ChooseServiceData(actions=ChooseServiceActions.pedicure))
    builder.button(text="🫦Перманентний макіяж",callback_data=ChooseServiceData(actions=ChooseServiceActions.permanent))

    builder.adjust(2,1)

    return builder.as_markup()
