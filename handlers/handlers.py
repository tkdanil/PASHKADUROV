from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from sqlalchemy.ext.asyncio import async_sessionmaker
from logic.bot_logic import BotLogic

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message, session_maker: async_sessionmaker):
    async with session_maker() as session:
        logic = BotLogic(session)
        if message.from_user:
            await message.answer(await logic.register_user(message.from_user.id, message.from_user.full_name))

@router.message(Command("status"))
async def cmd_status(message: Message, session_maker: async_sessionmaker):
    async with session_maker() as session:
        logic = BotLogic(session)
        if message.from_user:
            await message.answer(await logic.get_user_status(message.from_user.id))

@router.message(Command("vmpath"))
async def cmd_vmpath(message: Message, session_maker: async_sessionmaker):
    async with session_maker() as session:
        logic = BotLogic(session)
        if message.from_user and message.text:
            parts = message.text.split()
            if len(parts) != 4:
                await message.answer("Используйте: /vmpath <ip> <username> <password>")
                return
            _, ip, username, password = parts
            await message.answer(await logic.save_vm_path(message.from_user.id, ip, username, password))

@router.message(Command("check"))
async def cmd_check(message: Message, session_maker: async_sessionmaker):
    async with session_maker() as session:
        logic = BotLogic(session)
        if message.from_user:
            await message.answer(await logic.check_vm_connection(message.from_user.id))

@router.message(Command("ls"))
async def cmd_ls(message: Message, session_maker: async_sessionmaker):
    async with session_maker() as session:
        logic = BotLogic(session)
        if message.from_user:
            await message.answer(await logic.list_home_dir(message.from_user.id), parse_mode="Markdown")

@router.message(Command("cat"))
async def cmd_cat(message: Message, session_maker: async_sessionmaker):
    async with session_maker() as session:
        logic = BotLogic(session)
        if message.from_user:
            response = await logic.cat_text_files(message.from_user.id)
            if len(response) > 4096:
                for i in range(0, len(response), 4096):
                    await message.answer(response[i:i + 4096])
            else:
                await message.answer(response)
