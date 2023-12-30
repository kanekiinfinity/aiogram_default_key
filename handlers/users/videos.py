from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.default.forEntry import menuEntry
from keyboards.default.menu import menu
from keyboards.default.videos import menuVid

from loader import dp

@dp.message_handler(text="Boshqa foydali videolar")
async def show_menu(message: Message):
    await message.answer("Foydali videolar👇", reply_markup=menuVid)

@dp.message_handler(text="◀️Orqaga")
async def show_menu(message: Message):
    await message.answer("Darslarni tanlang👇", reply_markup=menu)

@dp.message_handler(text="GitHubda ro'yxatdan o'tish✈️")
async def show_menu(message: Message):
    await message.answer("https://www.youtube.com/watch?v=j34rltM-U-k")

@dp.message_handler(text="Online test tuzish🧮")
async def show_menu(message: Message):
    await message.answer("https://www.youtube.com/watch?v=-9UMaNM5WLk")

@dp.message_handler(text="UzbekCodersda tez sertifikat olish📄✅")
async def show_menu(message: Message):
    await message.answer("https://www.youtube.com/watch?v=3r6UlEtPbEw")

@dp.message_handler(text="Tekinga Canva Pro💸")
async def show_menu(message: Message):
    await message.answer("https://www.youtube.com/watch?v=LfmvfD--p2g")


@dp.message_handler(text="ChatGTP'da ro'yxatdan o'tish💁‍♂️")
async def show_menu(message: Message):
    await message.answer("https://www.youtube.com/watch?v=_hmq_hACBVM")