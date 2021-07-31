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


@pyrogram.Client.on_message(pyrogram.filters.command(["start"]))
async def start(bot, update):
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
