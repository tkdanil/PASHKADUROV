from aiogram import types, Router
from aiogram.filters import Command
from .keyboard import keyboard  # импорт из клавиатур
from .callbacks import callback_message  # импорт из коллбека

# Создаем экземпляр Router
router = Router()

async def process_start_command(message: types.Message):
    '''Команда start'''
    await message.answer(text="Привет!")

async def process_help_command(message: types.Message):
    '''Команда help'''
    await message.answer(text="Помощь: доступные команды - /start, /help, /status")

async def process_status_command(message: types.Message):
    '''Команда status'''
    await message.answer(text="Статус: бот работает и готов к взаимодействию!")

# Здесь описывается маршрутизация
def register_message_handlers():
    '''Маршрутизация обработчиков'''
    router.message.register(process_start_command, Command("start"))
    router.message.register(process_help_command, Command("help"))
    router.message.register(process_status_command, Command("status"))

    return router  # Возвращаем маршрутизатор для использования в основном файле

# В конце файла можно добавить строку для экспорта функций
all = [
    'register_message_handlers'
]