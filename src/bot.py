"""Main module for the bot"""

import re
import logging
from os import getenv

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.exceptions import TelegramBadRequest

TOKEN = getenv("BOT_TOKEN")
if TOKEN is None:
    raise ValueError("BOT_TOKEN is not set")

bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


@dp.message(CommandStart())
async def start(message: types.Message):
    """Welcome message for bot DM"""
    if message.from_user is not None:
        logging.info("User %s started bot", message.from_user.id)
    await message.reply(
        "Привет, я бот для администрирования чатов\nДобавь меня в чат для фильтрации сообщений"
    )


@dp.message()
async def filter_message(message: types.Message):
    """Filter messages for links and user tags."""
    url_pattern = r"https?://\S+|www\.\S+|t\.me/\S+"
    username_pattern = r"@\w+"
    if (
        message.text
        and message.sender_chat is not None
        and message.sender_chat.type != "channel"
    ):
        if re.search(url_pattern, message.text) or re.search(
            username_pattern, message.text
        ):
            try:
                logging.info(
                    "Deleting message: %s from user %s",
                    message.text,
                    (
                        message.from_user.username
                        if message.from_user is not None
                        else "unknown"
                    ),
                )
                await message.delete()
            except TelegramBadRequest as e:
                logging.error("Error deleting message: %s", e)


async def main():
    """Runing bot"""
    logging.info("Bot started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
