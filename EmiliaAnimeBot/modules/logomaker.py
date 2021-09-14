from EmiliaAnimeBot.events import register
from EmiliaAnimeBot import OWNER_ID
from EmiliaAnimeBot import telethn as tbot
import os
import random
from PIL import Image, ImageDraw, ImageFont


logopics = [
	
 "./EmiliaAnimeBot/resources/logopics/photo_2021-09-11_15-46-57.jpg"
 
]

logofonts = [
 
 "./EmiliaAnimeBot/resources/logofonts/Neon machine.ttf"
 
]


@register(pattern="^/logo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:

    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('My owner is Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open(random.choice(logopics))
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "blue"
    shadowcolor = "blue"
    font = ImageFont.truetype(random.choice(logofonts) , 250)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.1)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(100, 100, 100))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="Blue", stroke_width=23, stroke_fill="Black")
    fname2 = "Logo.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Mᴀᴅᴇ ʙʏ @BelDaizoraRobot Cʀᴇᴀᴛᴇʀ ʙʏ @Im_so_much_worse_than_you_think")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Report @PigasusSupport, {e}')

   
file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")


__mod_name__ = "Logos"

__help__ = """

`/logo` *:* Cʀᴇᴀᴛ ᴀ ʟᴏɢᴏ ᴡɪᴛʜ Tᴇxᴛ!

"""

