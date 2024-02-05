from MultiAzBot import *
from pyrogram import filters

@app.on_message(filters.command("id"))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"**Sənin ID**: `{message.from_user.id}`\n**{reply.from_user.first_name} ID**: `{reply.from_user.id}`\n**Söhbət ID**: `{message.chat.id}`"
        )
    else:
        message.reply(
            f"**Sənin ID**: `{message.from_user.id}`\n**Söhbət ID**: `{message.chat.id}`"
        )