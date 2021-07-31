import os
import sqlite3
import logging

from translation import Translation as tr
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import Config as C
from pyrogram import Client, filters
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, UsernameNotOccupied, ChatAdminRequired, PeerIdInvalid
SUPPORT_GROUP = C.SUPPORT_GROUP
OWNER_USERNAME = C.OWNER_USERNAME
UPDATES_CHANNEL = C.UPDATES_CHANNEL
logging.basicConfig(level=logging.INFO)

@Client.on_message(filters.incoming & filters.command(["start"]))
async def start(client, message):
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
        client.send_message(
                chat_id = message.chat.id,
                text=tr.START_TEXT.format(message.from_user.first_name, message.from_user.id),
	        disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                           InlineKeyboardButton("Join Updates Channel", url=f"https://t.me/{update_channel}"),
                           InlineKeyboardButton("Support Group", url=f"https://t.me/{support_group}")
                      ],
                     [
                           InlineKeyboardButton("🧑‍💻Devloper🧑‍💻", url=f"https://t.me/{owner_username}")
                     ]
                 ]
             ),
        parse_mode="markdown",
        reply_to_message_id=message.message_id
        )
            return
    client.send_message(message.chat.id,
        text=tr.START_TEXT.format(message.from_user.first_name, message.from_user.id),
        disable_web_page_preview=True,
	reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Updates Channel", url=f"https://t.me/{update_channel}"),
                    InlineKeyboardButton("Support Group", url=f"https://t.me/{support_group}")
                ],
                [
                    InlineKeyboardButton("🧑‍💻Devloper🧑‍💻", url=f"https://t.me/{owner_username}")
                ]
            ]
        ),
        parse_mode="markdown",
        reply_to_message_id=message.message_id
        )
