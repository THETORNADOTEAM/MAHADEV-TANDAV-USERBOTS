
"""Check if userbot awake or not . 

"""
import os
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, CMD_HELP
from userbot.utils import admin_cmd
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname

ALIVE_PIC = Config.ALIVE_PHOTTO
if ALIVE_PIC is None:
   ALIVE_PIC = "https://telegra.ph/file/8eff616d2c2a262304969.jpg"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

ALIVE_MESSAGE = Config.ALIVE_MSG
if ALIVE_MESSAGE is None:
   ALIVE_MESSAGE = "**π±ππΈβπΈπ»πΌπ πππΌβπΉππ ππ πΈππΈππΌ..π± \n\n\n**"
   ALIVE_MESSAGE += "`κ±α΄α΄α΄κ± \n\n\n`"
   ALIVE_MESSAGE += f"`α΄α΄Κα΄α΄Κα΄Ι΄: TELETHON-1.19.0 \n\n`"
   ALIVE_MESSAGE += f"`α΄Κα΄Κα΄Ι΄: PYTHON-3.8.5 \n\n`"
   ALIVE_MESSAGE += "`Ιͺ'ΚΚ Κα΄ α΄‘Ιͺα΄Κ Κα΄α΄ α΄α΄κ±α΄α΄Κ α΄ΙͺΚΚ α΄Κ α΄ΚΙ΄α΄ α΄Ι΄α΄κ± α΄Κ Κα΄α΄ κ±α΄‘Ιͺα΄α΄Κ α΄κ°κ° α΄α΄ α΄α΄Ι΄α΄α΄ΚΚΚ!β  \n\n`"
   ALIVE_MESSAGE += f"`κ±α΄α΄α΄α΄Κα΄ α΄Κα΄Ι΄Ι΄α΄Κ` :  @TANDAV_USERBOT_CHANNEL\n\n"
   ALIVE_MESSAGE += f"`κ±α΄α΄α΄α΄Κα΄/κ±α΄Ι’Ι’α΄κ±α΄Ιͺα΄Ι΄ Ι’Κα΄α΄α΄` :  @TANDAV_USERBOT_SUPPORT\n\n"
   ALIVE_MESSAGE += f"`α΄Κ α΄α΄Κα΄α΄ κ±α΄ ΚΚΙͺ α΄α΄Κα΄α΄ α΄α΄κ±α΄α΄Κπ₯`: {DEFAULTUSER} \n\n "
                
            
#@command(outgoing=True, pattern="^.awake$")
@borg.on(admin_cmd(pattern=r"awake"))
async def amireallyalive(awake):
    """ For .awake command, check if the bot is running.  """
    await awake.delete() 
    await borg.send_file(awake.chat_id, ALIVE_PIC,caption=ALIVE_MESSAGE)
