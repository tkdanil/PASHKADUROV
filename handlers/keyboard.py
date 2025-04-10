import aiogram.types


# TODO - создайте клавиатуру, которая будет появляться в сообщении либо находится там постоянно
# Статичная клавиатура ReplyKeyboardMarkup https://docs.aiogram.dev/en/v3.15.0/api/types/reply_keyboard_markup.html
# Динамически генерируемая клавиатура Keyboard builder https://docs.aiogram.dev/en/v3.15.0/utils/keyboard.html
# Примеры создания клавиатуры ReplyKeyboardMarkup https://habr.com/ru/articles/820733/#:~:text=%D0%98%D0%BC%D0%BF%D0%BE%D1%80%D1%82%D1%8B%20%D0%B2%20all_kb.py%3A
# Примеры создания клавиатуры Keyboard builder https://mastergroosha.github.io/aiogram-3-guide/buttons/


# Здесь создать клавиатуры
import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Получите токен вашего бота (убедитесь, что BOT_TOKEN установлен в переменных окружения)
API_TOKEN = os.getenv("7399928399:AAGVW6kBllbTUDSjfA4uPW1GI1qF2EXraM0", "7399928399:AAGVW6kBllbTUDSjfA4uPW1GI1qF2EXraM0")

bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher()


# Обработчик команды /start с использованием статической клавиатуры (ReplyKeyboardMarkup)
@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    # Создаем статическую клавиатуру с тремя кнопками
    static_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Опция 1")],
            [KeyboardButton(text="Опция 2")],
            [KeyboardButton(text="Опция 3")]
        ],
        resize_keyboard=True,      # Автоматически подбирает оптимальный размер кнопок
        one_time_keyboard=False    # Клавиатура остается после нажатия
    )
    await message.answer("Привет! Выберите одну из опций:", reply_markup=static_keyboard)


# Обработчик команды /menu с использованием динамически генерируемой клавиатуры (Keyboard Builder)
@dp.message_handler(commands=["menu"])
async def show_menu(message: types.Message):
    # Список опций для генерации кнопок динамически
    options = ["Пункт A", "Пункт B", "Пункт C", "Пункт D"]
    kb_builder = ReplyKeyboardBuilder()

    # Добавляем кнопки в клавиатуру
    for option in options:
        kb_builder.button(text=option)

    # Располагаем кнопки по 2 в ряд
    kb_builder.adjust(2)

    await message.answer("Выберите пункт из меню:", reply_markup=kb_builder.as_markup(resize_keyboard=True))


# Главная корутина для запуска бота (без использования executor)
async def main():
    # Параллельный запуск поллинга
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())

