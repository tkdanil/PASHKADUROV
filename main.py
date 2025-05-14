import logging
import asyncio
from aiogram import Bot, Dispatcher,types
from config import TOKEN
from handlers import register_message_handlers, bot_commands
from db import async_create_table


# Настройка логирования
logging.basicConfig(level=logging.INFO)


async def main():


    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # Здесь функция для вызова хендлеров из handlers.py
    await register_message_handlers(dp)

    # Здесь вызов меню с командами бота
    await bot.set_my_commands(bot_commands, types.BotCommandScopeDefault())

    # Запуск бота в polling-режиме
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(async_create_table())
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("End Script!")