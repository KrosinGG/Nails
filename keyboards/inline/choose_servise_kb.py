from aiogram.utils.keyboard import InlineKeyboardBuilder

def servise_inline():
    builder = InlineKeyboardBuilder()

    builder.button(text="💅🏼 Маникюр",callback_data="a")
    builder.button(text="👣 Педикюр",callback_data="a")
    builder.button(text="🫦Перманентний макіяж",callback_data="a")

    builder.adjust(2,1)

    return builder.as_markup()
