from aiogram import Router, F, types
from aiogram.types import CallbackQuery

router = Router(name=__name__)

from keyboards.inline.permanent_kb import (
    PermanentActions,
    PermanentData,
    permanent_keyboard,
    enter_date
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