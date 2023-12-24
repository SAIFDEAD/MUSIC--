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
            InlineKeyboardButton(text=" ᴏᴡɴᴇʀ", url="https://t.me/{OWNER_ID}"),
            InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ ", url="https://t.me/SAIFALLBOT"),
        ],
        [
            InlineKeyboardButton(text=" ɢʀᴏᴜᴘ ", url="https://t.me/SAIFHELPGC"),
            InlineKeyboardButton(text="♨️ ᴅᴇᴠᴇʟᴏᴘᴇʀ ♨️", url="https://t.me/SAIF_DICTATOR"),
        ],
    ]
    return buttons
