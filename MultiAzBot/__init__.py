from pyrogram import Client
from AideTagger_Bot.config import *

app = Client(
    "AideTagger_Bot",
    api_id=API_ID 28979412,
    api_hash=API_HASH 0016b3e3a334036da841062673a60f7e,
    bot_token=BOT_TOKEN 6613265866:AAHBovwUJF57ZHLdh0k71xQqKmNGuzl0PXw,
    plugins=dict(root="AideTagger_Bot.plugins"),
)
