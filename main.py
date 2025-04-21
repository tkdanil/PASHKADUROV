# version1.0.0
import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import router


async def main():

    bot = Bot(token=TOKEN)
    dp = Dispatcher()

#Опредление для диспечера маршрутизация из handlers
    dp.include_router(router)



    # Запуск бота в polling-режиме
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
