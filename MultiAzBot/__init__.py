from pyrogram import Client
from MultiAzBot.config import *

app = Client(
    "MultiAzBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="MultiAzBot.plugins"),
)