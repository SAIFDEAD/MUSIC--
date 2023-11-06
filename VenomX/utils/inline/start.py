from pyrogram.types import InlineKeyboardButton

import config
from VenomX import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="♨️ ᴏᴡɴᴇʀ ♨️", url="https://t.me/Saif_Dictator"),
            InlineKeyboardButton(text="🎭 ᴄʜᴀɴɴᴇʟ 🎭", url="https://t.me/DEAD_SupportChat"),
        ],
        [
            InlineKeyboardButton(text="💫 ɢʀᴏᴜᴘ 💫", url="https://t.me/Dead_Groupchat"),
            InlineKeyboardButton(text="🛡 ᴍᴀɴᴇɢᴇʀ 🛡", url="https://t.me/DICMANAGEBOT"),
        ],
    ]
    return buttons
