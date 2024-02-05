
from MultiAzBot import *
from MultiAzBot.TextBase.Sehid.random_line import random_line
from pyrogram.errors import FloodWait
from pyrogram import Client, filters

@app.on_message(filters.command(["sehid"]))
async def _(client, message):
	await message.delete()
	await message.reply_text(await random_line('Sehid/sehid.txt'))
