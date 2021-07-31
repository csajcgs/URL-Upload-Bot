#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

import logging
import os
from translation import Translation as tr
from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO)


@Client.on_message(filters.incoming & filters.command(['help']))
def _help(client, message):
      client.send_message(message.chat.id,
        text=tr.HELP_MSG,
        disable_web_page_preview=True,
        parse_mode="markdown",
        reply_to_message_id=message.message_id
        )
