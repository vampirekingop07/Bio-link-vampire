import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "29308061"))
API_HASH = getenv("API_HASH", "462de3dfc98fd938ef9c6ee31a72d099")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", 8410426172))
MONGO_URI = os.getenv("MONGO_URI")
