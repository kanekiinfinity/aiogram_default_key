from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.default.forEntry import menuEntry, menuEntry1, menuEntry2
from keyboards.default.menu import menu

from loader import dp

@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
    await message.answer("Kurslarni tanlag👇", reply_markup=menu)

@dp.message_handler(text='Entry darslar')
async def show_menu(message: Message):
    await message.answer("Darsni tanlang👇", reply_markup=menuEntry)

@dp.message_handler(text="Bosh menyuga")
async def show_menu(message: Message):
    await message.answer("Darslarni tanlang", reply_markup=menu)

@dp.message_handler(text="Oldinga")
async def show_menu(message: Message):
    await message.answer("Darslarni tanlang👇",reply_markup=menuEntry1)


@dp.message_handler(text="Ortga")
async def show_menu(message: Message):
    await message.answer("Darslarni tanlang👇", reply_markup=menuEntry)


@dp.message_handler(text="Keyingisi")
async def show_menu(message: Message):
    await message.answer("Darslarni tanlang👇", reply_markup=menuEntry2)


@dp.message_handler(text="◀️Ortga")
async def show_menu(message: Message):
    await message.answer("Darslarni tanlang👇", reply_markup=menuEntry1)


