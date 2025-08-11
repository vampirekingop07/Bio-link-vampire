from pyrogram import filters
from pyrogram.types import CallbackQuery

def register(app):
    @app.on_callback_query(filters.regex("help"))
    async def help_button(_, query: CallbackQuery):
        await query.message.edit_text(
            "📚 Help Menu:\n\n"
            "/start - Start bot\n"
            "/broadcast - Broadcast to all\n"
            "Auto-delete users with links in bio or message",
            )
