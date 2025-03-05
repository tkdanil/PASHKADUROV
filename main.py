import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command

#Экземпляр бота и диспетчера
bot = Bot(token="7399928399:AAGVW6kBllbTUDSjfA4uPW1GI1qF2EXraM0")
dp = Dispatcher()

#Бот принимает команды, напрмер /start.
#Создание хенлер - обработчик сообщений, и будем возвращать сообщение
@dp.message(Command('start'))
async def process_start_command(message):
    await message.answer("Hi!")


@dp.message()
async def echo_message(messccage):
    await message.answer(message.text)

#фунция запуска проекта
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())