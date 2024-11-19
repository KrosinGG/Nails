from aiogram import Router, F, types
from aiogram.types import InputMediaPhoto


from keyboards.start_kb import ButtonText
from keyboards.inline.choose_servise_kb import servise_inline
from keyboards.inline.admin_menu_kb import admin_inline

router = Router(name=__name__)

@router.message(F.text == ButtonText.SIGN_UP)
async def choose_service(message: types.Message):
    await message.answer(
        text = "Оберіть бажану послугу 👇🏼",
        reply_markup = servise_inline()
    )

@router.message(F.text == ButtonText.ADMIN)
async def choose_service(message: types.Message):
    await message.answer(
        text = "Керуйте з легкісттю всіма процесами 🌸",
        reply_markup = admin_inline()
    )
    
@router.message(F.text == ButtonText.INFO)
async def choose_service(message: types.Message):
    await message.answer(
        text = "По всiм птанням: @wawa3d",
    )

@router.message(F.text == ButtonText.MASTERS_WORK)
async def choose_service(message: types.Message):
    await message.answer("Завантажую фото...")

    # URL фотографий
    photo_urls = [
        "https://images.thevoicemag.ru/upload/img_cache/b1a/b1ad88dca451354d49bf2f420873e2b9_cropped_666x833.jpg",
        "https://cdn.optipic.io/site-103475/wp-content/uploads/2022/02/frpk-010222.jpg"
    ]

    # Создаём список объектов InputMediaPhoto
    media = [InputMediaPhoto(media=url) for url in photo_urls]

    # Отправляем альбом
    await message.answer_media_group(media)
