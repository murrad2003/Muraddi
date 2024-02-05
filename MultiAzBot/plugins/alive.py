from MultiAzBot import *
from MultiAzBot.config import *
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Message
from datetime import datetime
from sys import version_info
from pyrogram import __version__
__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@app.on_message(filters.command(["alive"]))
async def Alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.delete()   
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("📢 Kanal", url=f"https://t.me/{CHANNEL}"),
                InlineKeyboardButton(
                    "🎧 Playlist", url=f"https://t.me/{PLAYLIST_NAME}"
                ),
            ]
        ]
    )

    alive = f"**Nədi nolub😒 {message.from_user.mention()}\n\nMənim Adım {BOT_USERNAME}**\n⚡ Mən Süper İşləyirəm\n👨🏻‍💻 Sahibim: [{BOT_USERNAME}](https://t.me/{OWNER_NAME})\n🏷️ Pyrogram Versiyası: `{__version__}`\n🔰 Python Versiyası: `{__python_version__}`\n👨‍🏭 İş Vaxtı Status: `{uptime}`"

    await message.reply_video(
        video=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )