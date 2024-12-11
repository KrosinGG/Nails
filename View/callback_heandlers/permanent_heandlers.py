from aiogram import Router, F, types
from aiogram.types import CallbackQuery

router = Router(name=__name__)

from keyboards.inline.permanent_kb import (
    PermanentActions,
    PermanentData,
    EnterDateServiceActions,
    EnterDateServiceDate,
    permanent_keyboard,
    enter_date,
    enter_time,
    enter_pay,
    confirm_entry,
    enter_reson_cancel
)

from keyboards.inline.choose_servise_kb import (
    ChooseServiceData,
    ChooseServiceActions
)

@router.callback_query(
        ChooseServiceData.filter(F.actions == ChooseServiceActions.permanent)
)
async def enter_permanent_service(
    call: CallbackQuery
):
    await call.message.edit_text(
        text="Оберіть послугу перманентного макіяжу",
        reply_markup=permanent_keyboard()
    )

@router.callback_query(
    PermanentData.filter(F.value == "permanen")
)
# нужно будет передавать услугу в клаву
async def sign_up_lips(
    call: CallbackQuery
):
    await call.message.edit_text(
        text="Оберіть зручну для Вас дату 📅",
        reply_markup=enter_date()
    )

@router.callback_query()
async def enter_date_service(
    call: CallbackQuery
):
    await call.message.edit_text(
        text="Оберіть зручний для Вас час ⏰",
        reply_markup=enter_time()
    )

@router.callback_query()
async def enter_pay_menu(call: CallbackQuery):
    await call.message.edit_text(
        text=f"<b>Послуга:</b> 💅🏼 Маникюр\n"
        "Час: 12:00\n\n"
        "Оберіть зручний спосіб оплати 💳",
        reply_markup=enter_pay()
    )

@router.callback_query()
async def confirm_entry_menu(call:CallbackQuery):
    await call.message.edit_text(
        text="Послуга: 💅🏼 Маникюр\n"
            "Дата: Сьогодні (21.10.24)\n"
            "Час: 12:00\n"
            "Оплата: 💸Готівка\n\n"
            "Якщо все вірно, нажміть \"Підтвердити ✅\"",
        reply_markup=confirm_entry()
    )

@router.callback_query()
async def wait_confirm_entry(call: CallbackQuery):
    await call.message.edit_text("Запит відправленний майстру. Дочекайтесь відповідь на Ваш запит ⏳")

@router.callback_query()
async def admin_confirm_entry(call: CallbackQuery):
    await call.message.edit_text(
        text="✍🏼 Новий запис на послугу:\n\n"
            "🌸 Послуга: Маникюр\n"
            "📅 Дата: Сьогодні (21.10.24)\n"
            "⏰ Час: 12:00\n"
            "💸 Оплата: Готівка\n"
            "👤 Клієнт: @username\n\n"
            "Підтвердіть запис, або ж відмініть його 👇🏼",
        reply_markup=confirm_entry()
    )

@router.callback_query()
async def entry_confirmed_user(call: CallbackQuery):
    await call.message.edit_text("Майстер підтвердив Ваш запис. З радістью будем очікувати о 12:00. До зустрічі 🌸")

@router.callback_query()
async def reason_cancel(call: CallbackQuery):
    await call.message.edit_text(
        "Вкажіть причину відмови, або ж напишіть клієнту @username",
        reply_markup=enter_reson_cancel()
    )