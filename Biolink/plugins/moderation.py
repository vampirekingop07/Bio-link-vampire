from pyrogram import filters
from pyrogram.types import Message
from bot.utils.database import add_warn, get_warns, mute_user, is_link_or_username

def register(app):
    @app.on_message(filters.group & ~filters.service)
    async def moderate_message(client, message: Message):
        if message.from_user and message.text:
            text = message.text.lower()
            if "http://" in text or "https://" in text or "t.me/" in text:
                if is_link_or_username(text):
                    await message.delete()
                    warns = await add_warn(message.chat.id, message.from_user.id)
                    if warns >= 4:
                        await mute_user(client, message.chat.id, message.from_user.id, reason="4 warnings")
                    else:
                        await message.reply_text(f"⚠️ Warning {warns}/3 for sending a link.")
