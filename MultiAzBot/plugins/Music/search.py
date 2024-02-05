from MultiAzBot import *
from pyrogram import filters
from youtube_search import YoutubeSearch
from pyrogram.types import Message

@app.on_message(filters.command(["search"]))
async def search(_, message: Message):
    m = await message.delete()  
    try:
        if len(message.command) < 2:
            await message.reply_text("**İstifadə:** `/song Uzaylılar hoşgeldiniz`")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("🔍 **Axtarılır...**")
        results = YoutubeSearch(query, max_results=5).to_dict()
        i = 0
        text = ""
        while i < 5:
            text += f"🏷️ **Başlıq:** __{results[i]['title']}__\n"
            text += f"⏱ **Dəqiqə:** `{results[i]['duration']}`\n"
            text += f"👁️‍🗨️ **Baxış:** `{results[i]['views']}`\n"
            text += f"📣 **Youtube Kanalı:** {results[i]['channel']}\n"
            text += f"🔗 **Link:** https://www.youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await m.edit(str(e))
