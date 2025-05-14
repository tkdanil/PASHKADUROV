__all__ = [
    'register_message_handlers'
]


# Работа c Router - https://docs.aiogram.dev/en/v3.14.0/dispatcher/router.html
# Пример работы с Router через декораторы @router - https://mastergroosha.github.io/aiogram-3-guide/routers/
# Пример работы с Router через функцию сборщик https://stackoverflow.com/questions/77809738/how-to-connect-a-router-in-aiogram-3-x-x#:~:text=1-,Answer,-Sorted%20by%3A


from aiogram import types, Router, filters, F
from .keyboard import keyboard_continue, keyboard_start  # импорт из клавиатур
from .callbacks import callback_message  # импорт из коллбека
from db import async_session, User
from sqlalchemy import select
# Создаем экземпляр Router


async def command_start_handler(message: types.Message):
    async with async_session() as session:
        query = select(User).where(message.from_user.id == User.user_id)
        result = await session.execute(query)
        if result.scalars().all():
            info="чтобы продолжить, вызовите команду /status"
            await message.answer(info)
        else:
            await  message.answer("выберите роль", reply_markup=keyboard_start)
            pass



async def command_help_handler(message: types.Message):
    """Команда help"""
    await message.answer(text="Справка!...")


# Здесь описывается маршрутизация
async def register_message_handlers(router: Router):
    """Маршрутизация обработчиков"""
    router.message.register(command_start_handler, filters.Command(commands=["start"]))
    router.callback_query.register(callback_message, F.data.endswith("_continue"))
