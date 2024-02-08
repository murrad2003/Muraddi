from MultiAzBot import *
from pyrogram import filters
from MultiAzBot.plugins.buttons import *
from MultiAzBot.TextBase.translator import Translation
from pyrogram.types import Message

AylinIMG = f"{START_IMG}"

@app.on_message(filters.private & filters.incoming & filters.command(['start']))
async def start(client, message: Message):
    user = message.from_user
    log_message = (
        f"🚀 **#YENİ_İSTİFADECİ Botu Başlatıldı!**\n\n"
        f"👤 **Ad:** {user.first_name}\n"
        f"👥 **Soyad:** {user.last_name}\n"
        f"🔖 **Tag Adı:** @{user.username}\n"
        f"🆔 **İstifadəçi ID:** ({user.id})\n"
        "Test"
    )
    await client.send_message(LOG_CHANNEL, log_message)
    await message.reply_photo(
        AylinIMG,  # AylinIMG'yi kendi başlatma görselinizle değiştirmelisiniz
        caption=Translation.START_TEXT.format(message.from_user.mention, BOT_USERNAME, OWNER_NAME, BOT_NAME),
        reply_markup=START_BUTTONS
    )
