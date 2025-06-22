__all__ = [
    'bot_commands'
]


from aiogram import types


# bot.set_my_command() - https://docs.aiogram.dev/en/v3.18.0/api/methods/set_my_commands.html
# BotCommand - https://docs.aiogram.dev/en/v3.18.0/api/types/bot_command.html#aiogram.types.bot_command.BotCommand
# Пример настройки меню команд - https://habr.com/ru/articles/820733/#:~:text=%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0%20%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%BC%D0%B5%D0%BD%D1%8E%20%D1%87%D0%B5%D1%80%D0%B5%D0%B7%20%D0%BA%D0%BE%D0%B4%3A


# Здесь создать список команд
bot_commands = [
    types.BotCommand(command="start", description="Запуск бота"),
    types.BotCommand(command="status", description="Информация о пользователе"),
    types.BotCommand(command="vmpath", description="Указать адрес виртуальной машины"),
    types.BotCommand(command="check", description="Проверить подключение к ВМ"),
    types.BotCommand(command="ls", description="Список файлов в домашнем каталоге"),
    types.BotCommand(command="cat", description="Содержимое текстовых файлов"),
]