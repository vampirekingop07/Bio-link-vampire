import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pymongo import MongoClient

mongo_client = MongoClient("YOUR_MONGO_URI")
db = mongo_client["your_db_name"]

def has_link(text: str) -> bool:
    keywords = ["http://", "https://", "t.me/", "www.", "@"]
    return any(word in text.lower() for word in keywords)

async def delete_later(message: Message, delay: int):
    await asyncio.sleep(delay)
    try:
        await message.delete()
    except Exception as e:
        print(f"⚠️ Warning message delete error: {e}")

def register(app: Client):
    @app.on_message(filters.group & ~filters.service)
    async def moderate_message(client: Client, message: Message):
        if not message.from_user:
            return

        try:
            chat = await client.get_chat(message.from_user.id)
            bio = getattr(chat, "bio", "") or ""
        except Exception as e:
            print(f"⚠️ Bio fetch error: {e}")
            bio = ""

        if has_link(bio):
            try:
                await message.delete()
                warn_msg = await message.reply_text(
    f"⚠️ {message.from_user.mention}, aapke bio mein link ya username hone ki wajah se aapka message delete kar diya gaya hai."
                )
                asyncio.create_task(delete_later(warn_msg, 10))
            except Exception as e:
                print(f"⚠️ Message delete/reply error: {e}")

def get_all_groups():
    return list(db.groups.find({}))

def get_all_users():
    return list(db.users.find({}))
