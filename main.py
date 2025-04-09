# version1.0.1
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    BotCommand
)
from config import TOKEN  # Убедитесь, что токен в config.py


async def on_startup(bot: Bot):
    """
    Устанавливает список команд для бота при старте.
    """
    commands = [
        BotCommand(command="start", description="Запустить бота"),
        BotCommand(command="help", description="Получить справку"),
        BotCommand(command="status", description="Проверить статус бота")
    ]
    await bot.set_my_commands(commands)


def register_message_handlers(dp: Dispatcher):
    """
    Регистрирует хендлеры для обработки команд.
    """

    @dp.message_handler(commands=["start"])
    async def start_handler(message: types.Message):
        """Обработчик команды /start с инлайн-клавиатурой"""
        inline_kb = InlineKeyboardMarkup(row_width=2)
        inline_kb.add(
            InlineKeyboardButton("Инлайн 1", callback_data="option1"),
            InlineKeyboardButton("Инлайн 2", callback_data="option2")
        )
        await message.answer("Привет! Выберите опцию (инлайн клавиатура):",
                           reply_markup=inline_kb)

    @dp.message_handler(commands=["help"])
    async def help_handler(message: types.Message):
        """Обработчик команды /help с постоянной клавиатурой"""
        reply_kb = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Кнопка A"), KeyboardButton("Кнопка B")],
                [KeyboardButton("Кнопка C"), KeyboardButton("Кнопка D")]
            ],
            resize_keyboard=True,
            one_time_keyboard=False
        )
        help_text = (
            "Справка:\n"
            "• /start – запуск бота и демонстрация инлайн клавиатуры\n"
            "• /help – получить справочную информацию с постоянной клавиатурой\n"
            "• /status – проверка состояния бота\n\n"
            "Попробуйте нажать на кнопки клавиатуры."
        )
        await message.answer(help_text, reply_markup=reply_kb)

    @dp.message_handler(commands=["status"])
    async def status_handler(message: types.Message):
        """Обработчик команды /status"""
        await message.answer("✅ Бот работает корректно!")


async def main():
    """
    Основная функция запуска бота.
    """
    bot = Bot(token='7399928399:AAGVW6kBllbTUDSjfA4uPW1GI1qF2EXraM0', parse_mode="HTML")  # Используем токен из конфига
    dp = Dispatcher(bot)

    # Регистрация хендлеров
    register_message_handlers(dp)

    # Установка команд меню
    await on_startup(bot)

    # Запуск бота
    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())
