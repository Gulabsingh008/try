from motor.motor_asyncio import AsyncIOMotorClient
from bot.config import MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)
db = client['telegram_bot']
