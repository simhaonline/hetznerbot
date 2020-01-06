#!/usr/bin/env python
# -*- coding: utf-8 -*-
from uuid import uuid4
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.utils.helpers import escape_markdown
import json
import logging
import os
from hetzner import *

logging.basicConfig(filename='/tmp/hetznerbot.log',level=logging.INFO, format='%(asctime)s %(message)s')
hetzner_api_token = os.getenv('HETZNER_API_TOKEN', '')
telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN', '')

def get_projects(update, context):
    """ Send all projects on hetzner """
    update.message.reply_text('Projects:')

def get_servers(update, context):
    """ Send a list of all servers """
    update.message.reply_text('Servers:')

def add_server(update, context):
    """ Add server """
    update.message.reply_text('Server added')

def rm_server(update, context):
    """ Remove server """
    update.message.reply_text('Server removed!')

def get_networks(update, context):
    """ Send a list of all networks """
    update.message.reply_text('Networks:')

def get_backups(update, context):
    """ Send a list of all backups """
    update.message.reply_text('Backup:')

def error(update, context):
    """Log Errors caused by Updates."""
    logging.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    updater = Updater(telegram_bot_token, use_context=True)
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("getprojects", get_projects))
    dp.add_handler(CommandHandler("getservers", get_servers))
    dp.add_handler(CommandHandler("addserver", add_server))
    dp.add_handler(CommandHandler("rmserver", rm_server))
    dp.add_handler(CommandHandler("getnetworks", get_networks))
    dp.add_handler(CommandHandler("getbackups", get_backups))    

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
