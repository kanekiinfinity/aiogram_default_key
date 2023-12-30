from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuVid = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Online test tuzish🧮"),
        ],
        [
            KeyboardButton(text="GitHubda ro'yxatdan o'tish✈️"),
            KeyboardButton(text="UzbekCodersda tez sertifikat olish📄✅"),
        ],
        [
            KeyboardButton(text="Tekinga Canva Pro💸"),
            KeyboardButton(text="ChatGTP'da ro'yxatdan o'tish💁‍♂️"),
        ],
        [
            KeyboardButton(text="◀️Orqaga"),
        ],
    ],

    resize_keyboard=True
)