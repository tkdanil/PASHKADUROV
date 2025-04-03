__all__ = [
    'register_message_handlers'
]


# TODO - Опишите вызов функций обработчиков через маршрутизацию
# Работа c Router - https://docs.aiogram.dev/en/v3.14.0/dispatcher/router.html
# Пример работы с Router через декораторы @router - https://mastergroosha.github.io/aiogram-3-guide/routers/
# Пример работы с Router через функцию сборщик https://stackoverflow.com/questions/77809738/how-to-connect-a-router-in-aiogram-3-x-x#:~:text=1-,Answer,-Sorted%20by%3A


from aiogram import types, Router
from aiogram.filters import Command
from .keyboard import keyboard  # импорт из клавиатур
from .callbacks import callback_message  # импорт из коллбека


async def process_start_command(message: types.Message):
    '''Команда start'''
    await message.answer(text="Привет!")


# Здесь описывается маршрутизация
def register_message_handlers():
    '''Маршрутизация обработчиков'''
    pass
