import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", 12345))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", 123456789))
MONGO_URI = os.getenv("MONGO_URI")
