from bot.database.mongo import db

async def is_premium(user_id):
    user = await db.users.find_one({"_id": user_id})
    return user and user.get("premium", False)

async def add_user(user_id, premium=False):
    await db.users.update_one(
        {"_id": user_id},
        {"$set": {"premium": premium}},
        upsert=True
    )

async def get_random_file(premium=False):
    query = {"premium": True} if premium else {"premium": False}
    return await db.files.aggregate([{"$match": query}, {"$sample": {"size": 1}}]).to_list(length=1)

async def save_file(file_id, premium=False):
    await db.files.insert_one({
        "file_id": file_id,
        "premium": premium
    })
