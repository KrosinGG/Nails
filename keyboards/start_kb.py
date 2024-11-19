from aiogram.utils.keyboard import ReplyKeyboardBuilder

class ButtonText:
    SIGN_UP = "💅🏼 Зробити запис"
    MASTERS_WORK = "📷 Роботи Майстрів"
    INFO = "ℹ️ Консультаiя"
    ADMIN = "⚙️ Админ меню"

def star_keyboard():
    builder = ReplyKeyboardBuilder()

    builder.button(text=ButtonText.SIGN_UP)
    builder.button(text=ButtonText.MASTERS_WORK)
    builder.button(text=ButtonText.INFO)
    builder.button(text=ButtonText.ADMIN)

    builder.adjust(1,2)
    
    return builder.as_markup(resize_keyboard=True)