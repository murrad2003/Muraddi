import os
from MultiAzBot.TextBase.translator import Translation
from MultiAzBot.plugins.buttons import *
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from MultiAzBot import *


@app.on_callback_query()
async def cb_data(client, message):
    if message.data == "home":
        await message.message.edit_text(
            text=Translation.START_TEXT.format(message.from_user.mention, BOT_USERNAME, OWNER_NAME, BOT_NAME),
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True,
        )
    elif message.data == "bh":
        await message.message.edit_text(
            text=Translation.BH_TEXT.format(message.from_user.mention, BOT_USERNAME, OWNER_NAME, BOT_NAME),
            reply_markup=BH_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "help":
        await message.message.edit_text(
            text=Translation.HELP_TEXT.format(message.from_user.mention, BOT_USERNAME, OWNER_NAME, BOT_NAME),
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "musıc":
        await message.message.edit_text(
            text=Translation.MUSIC_TEXT,
            reply_markup=MUSIC_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "tg":
        await message.message.edit_text(
            text=Translation.TELEGRAPH_TEXT,
            reply_markup=TELEGRAPH_BUTTONS,
            disable_web_page_preview=True
        ) 
    elif message.data == "eylence":
        await message.message.edit_text(
            text=Translation.EYLENCE_TEXT,
            reply_markup=EYLENCE_BUTTONS,
            disable_web_page_preview=True
        )        
    elif message.data == "sehıd":
        await message.message.edit_text(
            text=Translation.SEHID_TEXT,
            reply_markup=SEHID_BUTTONS,
            disable_web_page_preview=True
        ) 
    elif message.data == "oyun":
        await message.message.edit_text(
            text=Translation.OYUN_TEXT,
            reply_markup=OYUN_BUTTONS,
            disable_web_page_preview=True
        )        
    elif message.data == "sahib":
        await message.message.edit_text(
            text=Translation.SAHIB_TEXT,
            reply_markup=SAHIB_BUTTONS,
            disable_web_page_preview=True
        ) 
    elif message.data == "elave":
        await message.message.edit_text(
            text=Translation.ELAVELER_TEXT,
            reply_markup=ELAVE_BUTTONS,
            disable_web_page_preview=True
        )   
    elif message.data == "axtar":
        await message.message.edit_text(
            text=Translation.AXTARIS_TEXT,
            reply_markup=AXTAR_BUTTONS,
            disable_web_page_preview=True
        )   
    elif message.data == "tag":
        await message.message.edit_text(
            text=Translation.TAGGER_TEXT,
            reply_markup=TAGGER_BUTTONS,
            disable_web_page_preview=True
        )                
    else:
        await message.message.delete()
        