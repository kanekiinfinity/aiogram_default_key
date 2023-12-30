from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuEntry = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="00-DARS(Kirish)")
        ],
        [
            KeyboardButton(text="01-DARS"),
            KeyboardButton(text="02-DARS"),
        ],
        [
            KeyboardButton(text="03-DARS"),
            KeyboardButton(text="04-DARS"),
        ],
        [
            KeyboardButton(text="05-DARS"),
            KeyboardButton(text="06-DARS"),
        ],
        [
            KeyboardButton(text="Bosh menyuga"),
            KeyboardButton(text="Oldinga"),
        ],
    ],

    resize_keyboard=True
)

menuEntry1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="09-DARS"),
            KeyboardButton(text="10-DARS"),
        ],
        [
            KeyboardButton(text="11-DARS"),
            KeyboardButton(text="12-DARS"),
        ],
        [
            KeyboardButton(text="13-DARS"),
            KeyboardButton(text="14-DARS"),
        ],
        [
            KeyboardButton(text="Ortga"),
            KeyboardButton(text="Keyingisi"),
        ],
    ],

    resize_keyboard=True
)

menuEntry2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="15-DARS"),
            KeyboardButton(text="16-DARS(Amaliyot)"),
        ],
        [
            KeyboardButton(text="◀️Ortga")
        ],

    ],

    resize_keyboard=True
)