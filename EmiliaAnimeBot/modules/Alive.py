from telethon import events, Button, custom
import re, os
from EmiliaAnimeBot.events import register
from EmiliaAnimeBot import telethn as tbot
from EmiliaAnimeBot import telethn as tgbot
PHOTO = "https://telegra.ph/file/1682027883777783a43a9.mp4"
@register(pattern=("/alive"))
async def awake(event):
  PIKACHU = event.sender.first_name
  PIKACHU = "**✗ ɪ'ᴀᴍ VALT AOI ✗** \n\n"
  PIKACHU += "**✗ ɪ'ᴀᴍ beyblader bot for your group**\n\n"
  PIKACHU += "**✗ ɪ'ᴀᴍ ʜᴀᴠᴇ ᴘᴏᴡᴇʀ ғᴜʟʟ Cᴏᴍᴍᴇɴᴅs ᴡɪᴛʜ ./help**\n\n"
  PIKACHU += "**✗ Mʏ ʟᴇɢᴇɴᴅ ɪ ᴍᴇᴀɴ ᴍʏ ᴏᴡɴᴇʀ 🤗:** [✗Rohith✗](https://t.me/Rohith_no-1)\n\n"
  PIKACHU += "**♡ Python Version : 3.9**\n\n"
  BUTTON = [[Button.url("𝙎𝙐𝙋𝙋𝙊𝙍𝙏", "https://t.me/PigasusSupport"), Button.url("𝙐𝙋𝘿𝘼𝙏𝙀", "https://t.me/PigasusUpdates")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PIKACHU,  buttons=BUTTON)


mod_name = "alive"
command_list = ["alive"]




