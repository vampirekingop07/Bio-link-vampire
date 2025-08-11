from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import PeerIdInvalid
from Biolink.utils.database import has_link

def register(app):
    @app.on_message(filters.new_chat_members)
    async def handle_new_member(client, message: Message):
        for user in message.new_chat_members:
            if user.is_bot:
                continue

            try:
                user_info = await client.get_users(user.id)
                bio = getattr(user_info, "bio", "") or ""
            except Exception as e:
                print(f"⚠️ Failed to get bio: {e}")
                bio = ""

            first_name = user.first_name or ""
            full_text = (first_name + " " + bio).lower()

            # Check for link or username but do nothing now
            if await is_link_or_username(full_text):
                # Mute and delete removed
                # You can log or notify here if needed
                print(f"User {user.id} has link/username in bio or name, but no action taken.")
