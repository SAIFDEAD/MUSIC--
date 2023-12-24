import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from VenomX import LOGGER, app, userbot
from VenomX.core.call import Ayush
from VenomX.misc import sudo
from VenomX.plugins import ALL_MODULES
from VenomX.utils.database import get_banned_users, get_gbanned
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
        importlib.import_module("VenomX.plugins" + all_module)
    LOGGER("Innocent Music.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Ayush.start()
    try:
        await Ayush.stream_call("https://graph.org/file/ce82532492d587b3bcd00.mp4")
    except NoActiveGroupCall:
        LOGGER("Innocent").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Innocent Music Bot..."
        )
        exit()
    except:
        pass
    await Ayush.decorators()
    LOGGER("Innocent").info(
        "Imnocent Music Bot Started Successfully ⚡✨"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("Innocent").info("Stopping Innocent Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
