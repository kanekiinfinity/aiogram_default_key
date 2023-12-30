from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Entry darslar"),
            KeyboardButton(text="Boshqa foydali videolar"),

        ],
    ],

    resize_keyboard=True
)