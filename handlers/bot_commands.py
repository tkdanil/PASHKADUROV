from aiogram import types

# Здесь создаем список команд
set_my_commands = [
    types.BotCommand(command="/start", description="Начать взаимодействие с ботом"),
    types.BotCommand(command="/help", description="Получить помощь по командам"),
    types.BotCommand(command="/status", description="Проверить статус бота"),
]

async def setup_commands(bot):
    # Устанавливаем команды для бота
    await bot.set_my_commands(set_my_commands)