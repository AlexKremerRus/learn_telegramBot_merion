from telebot import TeleBot, types
from dotenv import load_dotenv
from loguru import logger
import os
import json
import messages

load_dotenv()

bot = TeleBot(os.getenv('BOT_TOKEN'))
logger.add("log.log", format="{time} {level} {message}", rotation="50MB")
logger.info("Bot started")

try:
    @bot.message_handler(commands=['start'])
    def send_welcome(message: types.Message):
        try:

            logger.info(f"message - {message.text}, from - {message.from_user.username}, in chat - {message.chat.id}")
            bot.send_message(message.chat.id, messages.START_MESSAGE )
        except Exception as e:
            logger.error(e)

    @bot.message_handler(commands=['help'])
    def send_help(message: types.Message):
        try:

            logger.info(f"message - {message.text}, from - {message.from_user.username}, in chat - {message.chat.id}")
            bot.send_message(message.chat.id, messages.HELP_MESSAGE)
        except Exception as e:
            logger.error(e)

    @bot.message_handler()
    def echo_all(message: types.Message):
        try:
            logger.info(f"message - {message.text}, from - {message.from_user.username}, in chat - {message.chat.id}")
            bot.send_message(message.chat.id, message.text)
        except Exception as e:
            logger.error(e)

    bot.infinity_polling(skip_pending=True)

except Exception as e:
    logger.error(e)

finally:
    logger.info("Bot stopped")
