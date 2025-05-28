from aiogram import Bot, Dispatcher, executor, types
from bot.config import BOT_TOKEN
from bot.handlers import start, get
import logging

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

start.register(dp)
get.register(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
