from telethon import events, Button, custom
import re, os
from EmiliaAnimeBot.events import register
from EmiliaAnimeBot import telethn as tbot
from EmiliaAnimeBot import telethn as tgbot
PHOTO = "https://telegra.ph/file/d7d927fe899b7415e21d7.jpg"
@register(pattern=("/alive"))
async def awake(event):
  PIKACHU = event.sender.first_name
  PIKACHU = "**✗ ɪ'ᴀᴍ 👸ʏᴜᴍɪ ✗** \n\n"
  PIKACHU += "**✗ ɪ'ᴀᴍ 👸ǫᴜᴇᴇɴ ᴏғ〘 ᴛɢ 〙**\n\n"
  PIKACHU += "**✗ ɪ'ᴀᴍ ʜᴀᴠᴇ ᴘᴏᴡᴇʀ ғᴜʟʟ Cᴏᴍᴍᴇɴᴅs ᴡɪᴛʜ ./help**\n\n"
  PIKACHU += "**✗ Mʏ ʟᴇɢᴇɴᴅ ɪ ᴍᴇᴀɴ ᴍʏ ᴏᴡɴᴇʀ 🤗:** [✗ᴄᴛᴢғᴀᴍɪʟʏ✗](https://t.me/ctzfamily)\n\n"
  PIKACHU += "**♡ Python Version : 3.9**\n\n"
  BUTTON = [[Button.url("𝙎𝙐𝙋𝙋𝙊𝙍𝙏", "https://t.me/PigasusSupport"), Button.url("𝙐𝙋𝘿𝘼𝙏𝙀", "https://t.me/PigasusUpdates")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PIKACHU,  buttons=BUTTON)


mod_name = "✗Alive✗"
