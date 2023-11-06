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
        [InlineKeyboardButton(text=_["🦋 ʜᴇʟᴘ 🦋"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["♨️ ᴏᴡɴᴇʀ ♨️"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["🕸 sᴜᴘᴘᴏʀᴛ 🕸"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text=_["⚔️ ᴄʜᴀɴɴᴇʟ ⚔️"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text="🎭 ᴅᴇᴠᴇʟᴏᴘᴇʀ 🎭", url="https://t.me/SAIF_DICTATOR"),
        ],
    ]
    return buttons
