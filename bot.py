#!/usr/bin/env python
# -*- coding: utf-8 -*-
from uuid import uuid4
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.utils.helpers import escape_markdown
import paho.mqtt.client as mqtt
import json
import logging
import os

logging.basicConfig(filename='/tmp/hetznerbot.log',level=logging.INFO, format='%(asctime)s %(message)s')
hetzner_api_token = os.getenv('HETZNER_API_TOKEN', '')
telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN', '')

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def error(update, context):
    """Log Errors caused by Updates."""
    logging.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(telegram_bot_token, use_context=True)
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("getprojects", start))
    dp.add_handler(CommandHandler("getservers", start))
    dp.add_handler(CommandHandler("addserver", start))
    dp.add_handler(CommandHandler("rmserver", start))
    dp.add_handler(CommandHandler("getnetworks", start))
    dp.add_handler(CommandHandler("getbackups", start))    

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
