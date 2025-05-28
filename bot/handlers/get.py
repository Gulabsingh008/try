from aiogram import types
from aiogram.dispatcher import Dispatcher
from bot.database.models import is_premium, get_random_file

async def get_cmd(message: types.Message):
    user_id = message.from_user.id
    premium = await is_premium(user_id)
    file = await get_random_file(premium)
    if file:
        await message.answer_document(file[0]['file_id'])
    else:
        await message.answer("No file found!")

def register(dp: Dispatcher):
    dp.register_message_handler(get_cmd, commands=['get'])
