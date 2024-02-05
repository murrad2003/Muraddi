from MultiAzBot import *
from pyrogram import filters
from MultiAzBot.database.carbon.errors import capture_err
from MultiAzBot.database.carbon.functions import make_carbon


@app.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "❌ Mətn daxil etmədin..."
        )
    if not message.reply_to_message.text:
        return await message.reply_text(
            "❌ Mətn daxil etmədin..."
        )
    m = await message.reply_text("🖼️ Carbonu hazırlayıram...")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("⚡ Artıq hazırdır! Göndərirəm...")
    await app.send_document(message.chat.id, carbon, caption=f"[{BOT_NAME}](https://t.me/{BOT_USERNAME}) tərəfindən {message.from_user.mention} üçün yaradıldı ✅")
    await m.delete()
    carbon.close()