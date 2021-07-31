import os
import sqlite3

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from translation import Translation
from pyrogram.types.bots_and_keyboards import InlineKeyboardButton, InlineKeyboardMarkup

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, UsernameNotOccupied, ChatAdminRequired, PeerIdInvalid
SUPPORT_GROUP = C.SUPPORT_GROUP
OWNER_USERNAME = C.OWNER_USERNAME
UPDATES_CHANNEL = C.UPDATES_CHANNEL


@pyrogram.Client.on_message(pyrogram.filters.command(["start"]))
async def start(bot, update):
    support_group = SUPPORT_GROUP
    owner_username = OWNER_USERNAME
    update_channel = UPDATES_CHANNEL
    if update_channel:
        try:
            user = client.get_chat_member(update_channel, message.chat.id)
            if user.status == "kicked":
               client.send_message(
                   chat_id=message.chat.id,
                   text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/UniversalBotsSupport).",
                   parse_mode="markdown",
                   disable_web_page_preview=True
               )
               return
        except UserNotParticipant:
            client.send_message(
                chat_id=message.chat.id,
                text="**Please Join My Updates Channel to use this Bot!**",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join Updates Channel", url=f"https://t.me/{update_channel}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.START_TEXT.format(update.from_user.first_name),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Source", url="https://github.com/Kirodewal/URLuploader-With-Hotstar"
                        ),
                        InlineKeyboardButton("Project Channel", url="https://t.me/HxBots"),
                    ],
                    [InlineKeyboardButton("Author", url="https://t.me/Kirodewal")],
                ]
            ),
            reply_to_message_id=update.message_id
        )
