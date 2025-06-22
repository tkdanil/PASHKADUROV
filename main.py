import asyncio
import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import TelegramObject

from config import BOT_TOKEN
from db.engine import create_async_engine, get_session_maker
from db.models import create_db_tables
from handlers.handlers import router as main_router
from handlers.bot_commands import private_commands


class DbSessionMiddleware:
    def __init__(self, session_maker):
        self.session_maker = session_maker

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        data["session_maker"] = self.session_maker
        return await handler(event, data)


async def main():
    logging.basicConfig(level=logging.INFO)
    if not BOT_TOKEN:
        logging.critical("Токен бота не найден!")
        return

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    # Инициализация БД
    async_engine = create_async_engine()
    async with async_engine.begin() as conn:
        await conn.run_sync(create_db_tables)
    session_maker = get_session_maker(async_engine)

    # Подключение middleware и роутеров
    dp.update.middleware(DbSessionMiddleware(session_maker))
    dp.include_router(main_router)

    # Очищаем очередь старых обновлений
    await bot.delete_webhook(drop_pending_updates=True)

    # Устанавливаем команды ПОСЛЕ инициализации всех компонентов и перед запуском
    await bot.set_my_commands(private_commands)

    logging.info("Бот запущен!")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
