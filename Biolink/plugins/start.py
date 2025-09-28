from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode

def register(app):
    @app.on_message(filters.command("start") & (filters.private | filters.group))
    async def start(_, message: Message):
        text = f"""👋 <b>Hello {message.from_user.first_name}!</b>

Welcome to <b>Bio Mute Bot</b> — your friendly group moderator 🤖

I help keep your group safe by monitoring bios for unwanted links and muting or banning violators automatically.

🚀 <i>Get started by adding me to your group!</i>

If you need help or updates, check the buttons below 👇"""
        
        buttons = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("✙ ʌᴅᴅ ϻє ɪη ʏσυʀ ɢʀσυᴘ ✙", url="https://t.me/Candyy_music_robot?startgroup=true")],
                [InlineKeyboardButton("˹ υᴘᴅᴧᴛєs ˼", url="https://t.me/kriti_bot_update")],
                [InlineKeyboardButton("˹ ʜєʟᴘ ᴧηᴅ ᴄσϻϻᴧηᴅs ˼", callback_data="help")]
            ]
        )

        photo_url = "https://files.catbox.moe/l5abdg.jpg"

        try:
            # Group mein photo bhejna kabhi kabhi permission issue de sakta hai
            await message.reply_photo(
                photo_url,
                caption=text,
                reply_markup=buttons,
                parse_mode=ParseMode.HTML
            )
        except Exception:
            # Agar photo nahi jaata to fallback ke liye sirf text bhej do
            await message.reply_text(
                text,
                reply_markup=buttons,
                parse_mode=ParseMode.HTML
            )
