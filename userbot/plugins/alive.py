# JassManak1125 

# Changes Made by Jass

# Thanks to Sipak bro and Aryan.. 
# animation Idea by @ItzSipak && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
import asyncio
import os
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, version
from userbot.utils import admin_cmd, sudo_cmd
from userbot import ALIVE_NAME, Lastupdate
from . import dcdef
from telethon.tl.types import ChannelParticipantsAdmins
# π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "MAHADEV TANDAV USERBOT"

# Thanks to Sipak bro and Aryan.. 
# animation Idea by @ItzSipak && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for DC(DARK COBRA)
global ghanti
ghanti = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/03e03334c8dc1c8e124d2.jpg"
file2 = "https://telegra.ph/file/974b08d63a0b0d967e778.jpg"
file3 = "https://telegra.ph/file/9aba3f1c2d3047a625da5.jpg"
""" =======================CONSTANTS====================== """


@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))

async def hmm(yes):
    chat = await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    await yes.delete()
    uptime = await dcdef.get_readable_time((time.time() - Lastupdate))
    pm_caption = "** πΌπ°π·π°π³π΄π πππ΄ππ±πΎπ πΈπ πΎπ½π»πΈπ½π΄**\n\n"
    pm_caption += "**Κα΄κ± α΄α΄κ±α΄α΄Κ, α΄α΄ α΄ΚΙͺα΄ α΄ α΄Ι΄α΄ κ±Κκ±α΄α΄α΄κ± α΄Κα΄ α΄‘α΄Κα΄ΙͺΙ΄Ι’ α΄α΄Κκ°α΄α΄α΄ΚΚ α΄κ± Ιͺα΄ κ±Κα΄α΄Κα΄ Κα΄...**\n\n"
    pm_caption += "β πππππππ πORNADO πππππππ  β\n\n"
    pm_caption += f"βΎ **α΄α΄Κα΄α΄Κα΄Ι΄ α΄ α΄Κκ±Ιͺα΄Ι΄** β {version.__version__}\n"
    pm_caption += "βΎ **κ±α΄α΄α΄α΄Κα΄ α΄Κα΄Ι΄Ι΄α΄Κ** β [α΄α΄ΙͺΙ΄](https://t.me/MAHADEV_TORNADO_USERBOT_SUPPORT)\n"
    pm_caption += "βΎ **ΚΙͺα΄α΄Ι΄κ±α΄**  β [πππππππ](https://github.com/SRIDHAR2021SIDDHARTH)\n"
    pm_caption += "βΎ **α΄α΄α΄ΚΚΙͺΙ’Κα΄ ΚΚ** β [πππππππ](https://github.com/SRIDHAR2021SIDDHARTH/MAHADEV-TANDAV-USERBOTS)\n\n"
    pm_caption += f"βΎ **α΄α΄α΄Ιͺα΄α΄** β {uptime}\n\n"
    pm_caption += f"βΎ **α΄Κ α΄α΄sα΄α΄Κ** β [{DEFAULTUSER}](tg://user?id={ghanti})\n"
    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    

