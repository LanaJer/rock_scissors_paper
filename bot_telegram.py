#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards.
"""
import logging
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler


from dotenv import load_dotenv

from rock_paper_scissors import rock_scissors_paper_round

from rock_paper_scissors import get_result_text

load_dotenv()

BUTTON_NAMES = {
    'r': 'Rock',
    's': 'Scissors',
    'p': 'Paper',
}


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    keyboard = [
        [
            InlineKeyboardButton("Rock⛰", callback_data='r'),
            InlineKeyboardButton("Scissors✂️", callback_data='s')
        ],
        [
            InlineKeyboardButton("Paper📃", callback_data='p')
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    context.user_data['user_score'] = 0
    context.user_data['bot_score'] = 0

    update.message.reply_text('Please choose:', reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    if 'user_score' not in context.user_data:
        context.user_data['user_score'] = 0
    if 'bot_score' not in context.user_data:
        context.user_data['bot_score'] = 0

    result = rock_scissors_paper_round(query.data)

    if result is True:
        context.user_data['user_score'] += 1
    elif result is False:
        context.user_data['bot_score'] += 1

    text = (
        f"Your choice: {BUTTON_NAMES[query.data]}\n"
        f"Result: {get_result_text(result)}\n"
        f"Your score: {context.user_data['user_score']}\n"
        f"Bot score: {context.user_data['bot_score']}"

    )

    keyboard = [
        [
            InlineKeyboardButton("Rock⛰", callback_data='r'),
            InlineKeyboardButton("Scissors✂️", callback_data='s'),
            InlineKeyboardButton("Paper📃", callback_data='p')
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(text=text, reply_markup=reply_markup)

    print('callback:', update.callback_query.data)


def help(update, context):
    update.message.reply_text("Use /start to test this bot.")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(os.getenv("BOT_TOKEN"), use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()