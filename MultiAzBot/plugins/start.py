from MultiAzBot import *
from pyrogram import filters
from MultiAzBot.plugins.buttons import *
from MultiAzBot.TextBase.translator import Translation
from pyrogram.types import Message

AylinIMG = f"{START_IMG}"


@app.on_message(filters.private & filters.incoming & filters.command(['start']))
async def start(client, message: Message):
    user = message.from_user
    log_message = f"{user.first_name} {user.last_name} (@{user.username}) ({user.id}) Test"
    await client.send_message(LOG_CHANNEL, log_message)
    await message.reply_photo(
        AylinIMG,  # AylinIMG'yi kendi başlatma görselinizle değiştirmelisiniz
        caption=Translation.START_TEXT.format(message.from_user.mention, BOT_USERNAME, OWNER_NAME, BOT_NAME),
        reply_markup=START_BUTTONS
    )
