from pyrogram import filters
from pyrogram.types import Message
from Biolink.config import OWNER_ID
from Biolink.utils.database import get_all_groups, get_all_users  # Ensure these exist

def register(app):
    @app.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
    async def broadcast_cmd(_, message: Message):
        if not message.reply_to_message:
            return await message.reply("Reply to a message to broadcast.\n\nUse:\n`/broadcast` - To all groups\n`/broadcast -user` - To all users")

        mode = "group"
        if len(message.command) > 1 and message.command[1] == "-user":
            mode = "user"

        await message.reply(f"✅ Starting broadcast to {mode}s...")

        if mode == "group":
            groups = await get_all_groups()
            sent, failed = 0, 0
            for chat in groups:
                try:
                    await message.reply_to_message.copy(chat["chat_id"])
                    sent += 1
                except Exception:
                    failed += 1

        else:  # mode == "user"
            users = await get_all_users()
            sent, failed = 0, 0
            for user in users:
                try:
                    await message.reply_to_message.copy(user["user_id"])
                    sent += 1
                except Exception:
                    failed += 1

        await message.reply(f"📢 Broadcast complete!\n✅ Sent: {sent}\n❌ Failed: {failed}")
