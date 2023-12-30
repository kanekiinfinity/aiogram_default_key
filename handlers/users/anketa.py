from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, state

from loader import dp
from states.personalData import PersonalData
@dp.message_handler(Command('anketa'))
async def anketa_test(message: types.Message):
    await message.answer("To'liq ismingizni kiriting✅")
    await PersonalData.fullname.set()

@dp.message_handler(state=PersonalData.fullname)
async def anketa_fullname(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data(
        {"name": fullname}
    )
    await message.answer("Emailingizni kiriting📩")
    await PersonalData.next()

@dp.message_handler(state=PersonalData.email)
async def answer_email(message: types.Message, state: FSMContext):
    email = message.text

    await state.update_data(
        {"email": email}
    )

    await message.answer("Telefon raqam kiriting📲")

    await PersonalData.next()

@dp.message_handler(state=PersonalData.phoneNum)
async def answer_phone(message: types.Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {"phone": phone}
    )
    data = await state.get_data()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")

    msg = "📄Siz haqingizda qabul qilingan ma'lumotlar: \n"
    msg += f"✅Ismingiz - {name} \n"
    msg += f"📲Telefon raqamingiz - {phone} \n"
    msg += f"📩Emailingiz - {email}"

    await message.answer(msg)

    await state.finish()