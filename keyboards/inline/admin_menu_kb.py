from aiogram.utils.keyboard import InlineKeyboardBuilder

def admin_inline():
    builder = InlineKeyboardBuilder()

    builder.button(text="😻 Майстри",callback_data="a")
    builder.button(text="💅🏼 Послуги",callback_data="a")
    builder.button(text="📅 Вільні дні",callback_data="a")
    builder.button(text="⏰ Вільні години",callback_data="a")
    builder.button(text="📷 Роботи майстрів",callback_data="a")
    builder.button(text="✍🏼 Записи",callback_data="a")
    builder.button(text="📊 Статистика",callback_data="a")
    builder.button(text="📢 Розсилка",callback_data="a")

    builder.adjust(1,1,2,1)

    return builder.as_markup()
