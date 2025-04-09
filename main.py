# version1.0.0
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    BotCommand
)
from config import TOKEN


async def on_startup(bot: Bot):
    """
    Устанавливает список команд для бота.
    Эти команды будут видны пользователю при вводе символа «/».
    """
    commands = [
        BotCommand(command="start", description="Запустить бота"),
        BotCommand(command="help", description="Получить справку"),
        BotCommand(command="status", description="Проверить статус бота")
    ]
    await bot.set_my_commands(commands)


def register_message_handlers(dp: Dispatcher):
    """
    Регистрирует хендлеры для обработки команд и создания клавиатур.
    """

    @dp.message_handler(commands=["start"])
    async def start_handler(message: types.Message):
        # Создание инлайн-клавиатуры, которая появляется в сообщении
        inline_kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Инлайн 1", callback_data="option1")],
            [InlineKeyboardButton(text="Инлайн 2", callback_data="option2")]
        ])
        await message.answer("Привет! Выберите опцию (инлайн клавиатура):", reply_markup=inline_kb)

    @dp.message_handler(commands=["help"])
    async def help_handler(message: types.Message):
        # Создание постоянной (reply) клавиатуры, которая остается под полем ввода
        reply_kb = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Кнопка A"), KeyboardButton(text="Кнопка B")],
                [KeyboardButton(text="Кнопка C"), KeyboardButton(text="Кнопка D")]
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
        await message.answer("Бот работает корректно!")


async def main():
    """
    Основная функция для настройки и запуска бота.
    Здесь:
    • Создаем экземпляр бота с указанным TOKEN
    • Регистрируем хендлеры для команд и клавиатур
    • Устанавливаем меню команд, которое появится при вводе «/»
    • Запускаем поллинг для получения обновлений.
    """
    bot = Bot(token='7399928399:AAGVW6kBllbTUDSjfA4uPW1GI1qF2EXraM0', parse_mode="HTML")
    dp = Dispatcher(bot)

    # Регистрация хендлеров для сообщений
    register_message_handlers(dp)

    # Установка меню команд бота (/start, /help, /status)
    await on_startup(bot)

    # Запуск бота в режиме polling
    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())
