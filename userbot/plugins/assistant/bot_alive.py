from telethon import events

from userbot import ALIVE_NAME, bot

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ππΈβπΈπ»πΌπ TORNADO πππΌβπΉππ"
PM_IMG = "https://telegra.ph/file/6f739e51ecfc6bf7ee9de.jpg"
pm_caption = "β₯ **ASSISTANT IS:** `ONLINE`\n\n"
pm_caption += "β₯ **SYSTEMS STATS**\n"
pm_caption += "β₯ **Telethon Version:** `1.15.0` \n"
pm_caption += "β₯ **Python:** `3.8.6` \n"
pm_caption += "β₯ **Database Status:**  `Functional`\n"
pm_caption += "β₯ **Current Branch** : `master`\n"
pm_caption += f"β₯ **Version** : `2.0`\n"
pm_caption += f"β₯ **My Boss** : {DEFAULTUSER} \n"
pm_caption += "β₯ **Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "β₯ **License** : [GNU General Public License v3.0](github.com/SRIDHAR2021SIDDHARTH/MAHADEV-TANDAV-USERBOTS/blob/master/LICENSE)\n"
pm_caption += "β₯ **Copyright** : By [ππΈβπΈπ»πΌπ TORNADO πππΌβπΉππ](https://t.me/MAHADEV_TORNADO_USERBOT_OFFICIAL)\n"
pm_caption += "[Assistant By ππΈβπΈπ»πΌπ TORNADO πππΌβπΉππ](https://t.me/MAHADEV_TORNADO_USERBOT_SUPPORT)"

# only Owner Can Use it
@tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
