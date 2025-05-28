from aiogram import types
from aiogram.dispatcher import Dispatcher

async def start_cmd(message: types.Message):
    btn = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton("🔥 Join Channel", url="https://t.me/YourChannel")
    )
    await message.answer_photo(
        photo="https://example.com/image.jpg",
        caption="Welcome to the bot!",
        reply_markup=btn
    )

def register(dp: Dispatcher):
    dp.register_message_handler(start_cmd, commands=['start'])
