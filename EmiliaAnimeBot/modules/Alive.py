from telethon import events, Button, custom
import re, os
from EmiliaAnimeBot.events import register
from EmiliaAnimeBot import telethn as tbot
from EmiliaAnimeBot import telethn as tgbot
PHOTO = "https://telegra.ph/file/082b9f21f46271f662ad4.jpg"
@register(pattern=("/alive"))
async def awake(event):
  PIKACHU = event.sender.first_name
  PIKACHU = "**♡ I,m Serena** \n\n"
  PIKACHU += "**♡ I'm Working Properly**\n\n"
  PIKACHU += "**♡ Serena : 2.0 LATEST**\n\n"
  PIKACHU += "**♡ My Master :** [AASF](https://t.me/AASFCYBERKING)\n\n"
  PIKACHU += "**♡ Python Version : 3.9**\n\n"
  BUTTON = [[Button.url("𝙎𝙐𝙋𝙋𝙊𝙍𝙏", "https://t.me/PigasusSupport"), Button.url("𝙐𝙋𝘿𝘼𝙏𝙀", "https://t.me/PigasusUpdates")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PIKACHU,  buttons=BUTTON)


mod_name = "Alive⚜️"
