import logging

from aiogram.types import CallbackQuery
from sqlalchemy import insert
from db import User, async_session
import string
from random import choices
import logging

# Callback_query_handler - это функция, которая позволяет обрабатывать коллбек-запросы от пользователей.
# Коллбэк-запрос - это запрос, который отправляется боту, когда пользователь нажимает кнопку в его чате.

# CallbackQuery https://docs.aiogram.dev/en/v3.15.0/api/types/callback_query.html
# Пример использования callback https://ru.stackoverflow.com/questions/1565436/%D0%9A%D0%B0%D0%BA-%D1%81%D0%B4%D0%B5%D0%BB%D0%B0%D1%82%D1%8C-%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA-%D0%BA%D0%BE%D0%BB%D0%B1%D0%B5%D0%BA%D0%BE%D0%B2-%D0%B2-aiogram-3#:~:text=%D0%94%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C%20%D0%BA%D0%BE%D0%BC%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%80%D0%B8%D0%B9-,1%20%D0%BE%D1%82%D0%B2%D0%B5%D1%82,-%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0%3A
# Пример использования инлайн-клавиатуры и CallBack https://habr.com/ru/articles/820877/
# Пример обработчика для callback с F.data для aiogram3 https://ru.stackoverflow.com/questions/1565436/%D0%9A%D0%B0%D0%BA-%D1%81%D0%B4%D0%B5%D0%BB%D0%B0%D1%82%D1%8C-%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA-%D0%BA%D0%BE%D0%BB%D0%B1%D0%B5%D0%BA%D0%BE%D0%B2-%D0%B2-aiogram-3#:~:text=%D0%94%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C%20%D0%BA%D0%BE%D0%BC%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%80%D0%B8%D0%B9-,1%20%D0%BE%D1%82%D0%B2%D0%B5%D1%82,-%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0%3A


async def callback_message(callback: CallbackQuery):
    """Ответ на кнопку"""



    await callback.message.answer("Успешно!")

async def callback_start_tutor(callback: CallbackQuery):
    """регестрация преподователя"""

    async with async_session() as session:
         """Что-то происходит"""
         chars = string.ascii_letters + string.digits + string.punctuation
         new_user = {
             "user_id": callback.from_user.id,
             "username": callback.from_user.username,
             "tutorcode": "".join(choices(chars, k = 6))
         }
         insert_query = insert(User).values(**new_user)
         await session.execute(insert_query)
         await session.commit()
         await callback.message.answer("Пользователь добавлен!")
         logging.info(f"Пользователь {callback.from_user.username} добавлен в базу данных с ролью преподователь!")
