from aiogram import types
from aiogram.dispatcher import  filters

from loader import dp

@dp.message_handler(is_reply=True, commands='user_id')
async def reply_filter(msg: types.Message):
    await msg.answer(msg.reply_to_message.from_user.id)

@dp.message_handler(content_types='contact', is_sender_contact=True)
@dp.message_handler(filters.IsSenderContact, content_types='contact')
async def reply_contact(msg: types.Message):
    await msg.answer('Raqamingiz qabul qilindi✅')

@dp.message_handler(is_forwarded=True)
async def reply_forward(msg: types.Message):
    await msg.answer('Men uzatilgan habarlarga javob bermayman🙅‍♂️')
