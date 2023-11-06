from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def queue_markup(
    _,
    DURATION,
    CPLAY,
    videoid,
    played: Union[bool, int] = None,
    dur: Union[bool, int] = None,
):
    not_dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
            ),
        ],
         [
            InlineKeyboardButton(
                text="♨️ ᴏᴡɴᴇʀ ♨️", url="https://t.me/SAIF_DICTATOR",
            ),
            InlineKeyboardButton(
                text="🐾 sᴜᴩᴩᴏʀᴛ 🐾", url="https://t.me/Dead_SupportChat",
            ),
        ],
    ]
    dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_2"].format(played, dur),
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
            ),
        ],
         [
            InlineKeyboardButton(
                text="♨️ ᴏᴡɴᴇʀ ♨️", url="https://t.me/SAIF_DICTATOR",
            ),
            InlineKeyboardButton(
                text="🌬 ᴄʜᴀɴɴᴇʟ 🌬 ", url="https://t.me/Dead_SupportChat",
            ),
        ],
    ]
    upl = InlineKeyboardMarkup(not_dur if DURATION == "Unknown" else dur)
    return upl


def queue_back_markup(_, CPLAY):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"queue_back_timer {CPLAY}",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
           ],
             [
            InlineKeyboardButton(
                text="♨️ ᴏᴡɴᴇʀ ♨️", url="https://t.me/DRDIC1",
            ),
            InlineKeyboardButton(
                text="💫 ʀᴇᴘᴏ 💫", url="https://telegra.ph/file/9733d82450e02472201a4.mp4",
            ),
        ],
        ]
    )
    return upl


def aq_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
         [
            InlineKeyboardButton(
                text=" ᴏᴡɴᴇʀ ", url="https://t.me/SAIF_DICTATOR",
            ),
            InlineKeyboardButton(
                text=" sᴜᴘᴘᴏʀᴛ ", url="https://t.me/Dead_SupportChat",
            ),
        ],
    ]
    return buttons
