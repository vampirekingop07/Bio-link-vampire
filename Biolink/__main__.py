from pyrogram import Client, idle
from Biolink.config import API_ID, API_HASH, BOT_TOKEN
from Biolink.plugins import start, welcome, broadcast, owner, callback
from Biolink.utils import database

app = Client(
    "bio_mute_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Register all plugin handlers
start.register(app)
welcome.register(app)
database.register(app)
broadcast.register(app)
owner.register(app)
callback.register(app)

async def main():
    await app.start()
    print("🤖 Bio Mute Bot is running...")
app.run()
