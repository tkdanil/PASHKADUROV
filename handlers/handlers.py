__all__=[
    "router",
]
from aiogram import types, Router
from aiogram.filters import Command
from .keyboard import main_keyboard

# Создаем экземпляр Router
router = Router()




@router.message(Command('help'))
async def process_start_command(message):
    await message.answer("хелп!",reply_markup=main_keyboard)


@router.message(Command(commands=["start",'status']))
async def process_start_command(message):
    await message.reply(f"{message.from_user.id},{message.from_user.username}")
