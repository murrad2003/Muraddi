import random
from MultiAzBot import *
from pyrogram import filters

@app.on_message(filters.command("mal"))
async def calculate_wealth(client, message):
    wealth_percent = random.randint(50, 100)
    user = message.reply_to_message.from_user
    user_name = user.first_name if not user.last_name else f"{user.first_name} {user.last_name}"
    await message.reply(f"{user_name} bu şəxsin %{wealth_percent} mal olduğunu bilirəm😹")

@app.on_message(filters.command("esq"))
async def calculate_wealth(client, message):
    wealth_percent = random.randint(50, 100)
    user = message.reply_to_message.from_user
    user_name = user.first_name if not user.last_name else f"{user.first_name} {user.last_name}"
    await message.reply(f"{user_name} ilə sənin eşq faizin %{wealth_percent} 💕")