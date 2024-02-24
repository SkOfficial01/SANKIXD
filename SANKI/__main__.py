import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from SANKI import LOGGER, app, userbot
from SANKI.core.call import SANKI
from SANKI.misc import sudo
from SANKI.plugins import ALL_MODULES
from SANKI.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("SANKI.plugins" + all_module)
    LOGGER("SANKI.plugins").info("sᴜᴄᴄᴇssғᴜʟʟʏ ɪᴍᴘᴏʀᴛᴇᴅ ᴀʟʟ ᴍᴏᴅᴜʟᴇs...")
    await userbot.start()
    await Sanki.start()
    try:
        await Sanki.stream_call("https://te.legra.ph/file/39b302c93da5c457a87e3.mp4")
    except NoActiveGroupCall:
        LOGGER("AarohiX").error(
            "ʙʀᴏ ᴠᴄ ᴛᴏ ᴏɴ ᴋᴀʀʟᴇ  ʟᴏɢ ɢʀᴏᴜᴘ\ᴄʜᴀɴɴᴇʟ ᴋɪ.\n\n ᴏɴ ᴋᴀʀᴋᴇ ᴀᴀ ᴛᴀʙ ᴛᴀᴋ ʙᴏᴛ ʙᴀɴᴅ ᴋᴀʀ ʀʜᴀ..."
        )
        exit()
    except:
        pass
    await Sanki.decorators()
    LOGGER("SANKI").info(
        "ᴍᴜsɪᴄ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ, ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ʟɪsᴛᴇɴ ʟᴀɢ ғʀᴇᴇ ᴍᴜsɪᴄ"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("SANKI").info("sᴏʀʀʏ ᴍᴇ ʙᴏᴛ ʙᴀɴᴅ ᴋʀ ʀʜᴀ ʜᴜ.....")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
