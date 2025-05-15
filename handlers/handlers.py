__all__ = [
    'register_message_handlers'
]


# Работа c Router - https://docs.aiogram.dev/en/v3.14.0/dispatcher/router.html
# Пример работы с Router через декораторы @router - https://mastergroosha.github.io/aiogram-3-guide/routers/
# Пример работы с Router через функцию сборщик https://stackoverflow.com/questions/77809738/how-to-connect-a-router-in-aiogram-3-x-x#:~:text=1-,Answer,-Sorted%20by%3A


from aiogram import types, Router, filters, F
from .keyboard import keyboard_continue, keyboard_start  # импорт из клавиатур
from .callbacks import callback_message, callback_start_tutor, start_student, callback_insert_tutorcode  # импорт из коллбека
from db import async_session, User
from sqlalchemy import select


# информации о статусе
status_string: str = """
UserId {}
UserName {}
"""

async def command_start_handler(message: types.Message):
    async with async_session() as session:
        query = select(User).where(message.from_user.id == User.user_id)
        result = await session.execute(query)
        if result.scalars().all():
            info="чтобы продолжить, вызовите команду /status"
            await message.answer(info)
        else:
            await  message.answer("выберите роль", reply_markup=keyboard_start)


async def command_status_handler(message: types.Message):
    async with async_session() as session:
        query = select(User).where(message.from_user.id == User.user_id)
        result = await session.execute(query)
        user = result.scalar()
        if user.tutorcode:
            info = status_string + "Код преподавателя: {}"
            info = info.format(user.user_id, user.username, user.tutorcode)

        if user.subscribe:
            code = str(user.subscribe)
            info = status_string + "Преподаватель: {}"
            query = select(User).where(code == User.tutorcode)
            result = await session.execute(query)
            tutor = result.scalar()
            try:
                info = info.format(user.user_id, user.username, tutor.username)
            except:
                info = info.format(user.user_id, user.username)
        await message.answer(info)




async def command_help_handler(message: types.Message):
    """Команда help"""
    await message.answer(text="Справка!...")


# Здесь описывается маршрутизация
async def register_message_handlers(router: Router):
    """Маршрутизация обработчиков"""
    router.message.register(command_start_handler, filters.Command(commands=["start"]))
    router.message.register(command_status_handler, filters.Command(commands=["status"]))
    router.callback_query.register(callback_message, F.data.endswith("_continue"))
    router.callback_query.register(callback_start_tutor, F.data.endswith("_tutor"))
    router.callback_query.register(callback_insert_tutorcode, F.data.endswith("_student"))
    router.message.register(start_student, F.text.startswith("tutorcode-"))

