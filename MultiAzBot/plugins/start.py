from MultiAzBot import *
from pyrogram import filters
from MultiAzBot.plugins.buttons import *
from MultiAzBot.TextBase.translator import Translation

AylinIMG = f"{START_IMG}"

@app.on_message(filters.private & filters.incoming & filters.command(['start']))
async def start(client, message):
    await message.reply_photo(
        AylinIMG,
        caption=Translation.START_TEXT.format(message.from_user.mention, BOT_USERNAME, OWNER_NAME, BOT_NAME),
        reply_markup=START_BUTTONS
    )