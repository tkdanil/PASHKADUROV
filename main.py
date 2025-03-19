#version 0.1.0
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from config import TOKEN

#Экземпляр бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

#Бот принимает команды, напрмер /start.
#Создание хенлер - обработчик сообщений, и будем возвращать сообщение
@dp.message(Command('start'))
async def process_start_command(message):
    await message.answer("Hi!")


@dp.message()
async def echo_message(message):
    await message.answer(message.text)

#фунция запуска проекта
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
