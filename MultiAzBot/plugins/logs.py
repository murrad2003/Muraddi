import asyncio
from pyrogram import filters
from pyrogram.errors import FloodWait
from MultiAzBot import *


@app.on_message(filters.command("log") & filters.user(OWNER_ID)) #
async def logger(client, msj):
    chat_id = msj.chat.id
    reply = msj.reply_to_message
    if reply:
        replyid = reply.id
        await client.delete_messages(chat_id, msj.id)
        await client.forward_messages(
            LOG_CHANNEL,
            from_chat_id=msj.chat.id,
            message_ids=replyid
        )
        await client.send_message(chat_id, f"{msj.from_user.mention} mesaj uğurla log qrupuna göndərildi.")
    else:
        await client.send_message(chat_id, f"Bir mesaja yanıt ver.")