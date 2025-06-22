from aiogram.types import BotCommand

private_commands = [
    BotCommand(command='start', description='✅ Запустить/Перезапустить бота'),
    BotCommand(command='status', description='ℹ️ Посмотреть статус'),
    BotCommand(command='vmpath', description='⚙️ Настроить подключение к ВМ'),
    BotCommand(command='check', description='🔍 Проверить подключение к ВМ'),
    BotCommand(command='ls', description='📂 Показать файлы в домашней директории'),
    BotCommand(command='cat', description='📄 Показать содержимое .txt файлов'),
    BotCommand(command='help', description='❓ Помощь')
]