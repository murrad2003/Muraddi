import random
from random import choice
from pyrogram.types import Message
from MultiAzBot import *
from pyrogram import filters


temalar = ["[Bura toxun](https://t.me/addtheme/sf158WSw7LWOtpvV) ",
" [Bura toxun](https://t.me/addtheme/bpcrFtP4qYu0DdnJ) " ,
" [Bura toxun](https://t.me/addtheme/aUFKCX7AQ3aQpDjp) " ,
" [Bura toxun](https://t.me/addtheme/L7HVQjC4UUyOfL9y) " ,
" [Bura toxun](https://t.me/addtheme/Qd4eBWTIOH4Ai3Zv) " ,
" [Bura toxun](https://t.me/addtheme/NightWolf) " ,
" [Bura toxun](https://t.me/addtheme/GreenBlack) " ,
" [Bura toxun](https://t.me/addtheme/TvldPzYmpG8LqkY3) " ,
" [Bura toxun](https://t.me/addtheme/Q4GuvNPpMvG59G6V) " ,
" [Bura toxun](https://t.me/addtheme/kGQaW0HHsjc7oFOv) " ,
" [Bura toxun](https://t.me/addtheme/z3E6vkceX0pfmo5P) " ,
" [Bura toxun](https://t.me/addtheme/poMW3amfnwUwOefI) " ,
" [Bura toxun](https://t.me/addtheme/l1felAbEVNQCN3NW) " ,
" [Bura toxun](https://t.me/addtheme/y6xMaSuBOmuGekHj) " ,
" [Bura toxun](https://t.me/addtheme/Fp6h6JpzXrWnjF9y) " ,
" [Bura toxun](https://t.me/addtheme/Purple_Grapes) " ,
" [Bura toxun](https://t.me/addtheme/xQNP1Jp2aklmldNx) " ,
" [Bura toxun](https://t.me/addtheme/ry0AgHsISs439fxi) " ,
" [Bura toxun](https://t.me/addtheme/ZHl93FYO9ja7hN81) " ,
" [Bura toxun](https://t.me/addtheme/gc2MlPyKHMBjw5WS) " ,
" [Bura toxun](https://t.me/addtheme/ciNZt5N6QCFjsrQI) " ,
" [Bura toxun](https://t.me/addtheme/bEKOF0v8XuLAFZ6P) " ,
" [Bura toxun](https://t.me/addtheme/IOSTelegramThemes2020_11july) " ,
" [Bura toxun](https://t.me/addtheme/DarkPink_1) " ,
" [Bura toxun](https://t.me/addtheme/Halloween_04) " ,
" [Bura toxun](https://t.me/addtheme/BlackBlue_ByYamila) " ,
" [Bura toxun](https://t.me/addtheme/NewYorkNyVK) " ,
" [Bura toxun](https://t.me/addtheme/blackcircles_ByYamila) " ,
" [Bura toxun](https://t.me/addtheme/KINGByVK) " ,
" [Bura toxun](https://t.me/addtheme/MRPERFECTBYVK) " ,
" [Bura toxun](https://t.me/addtheme/ChanchiNeonByVK) " ,
" [Bura toxun](https://t.me/addtheme/SamurayByVK) " ,
" [Bura toxun](https://t.me/addtheme/NeonRocks_ByYamila) " ,
" [Bura toxun](https://t.me/addtheme/StichOhanaByVK) " ,
" [Bura toxun](https://t.me/addtheme/SkullDarkByVK) " ,
" [Bura toxun](https://t.me/addtheme/RedGirlByVK) " ,
" [Bura toxun](https://t.me/addtheme/SpidermanByVK) " ,
" [Bura toxun](https://t.me/addtheme/CuteMelodyByVK) " ,
" [Bura toxun](https://t.me/addtheme/YouAreBeautifulStichByVK) " ,
" [Bura toxun](https://t.me/addtheme/ManchesterUnitedByVK) "]



@app.on_message(filters.command("tema"))
async def tema(app: Client, msg: Message):
    await msg.reply(random.choice(temalar))