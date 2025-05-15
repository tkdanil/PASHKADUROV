__all__ = [
    "async_create_table",
    "async_sessionmaker",
]

from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from .models import Base

engine = create_async_engine(url="sqlite+aiosqlite:///instance/sqlite.db", echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)

async def async_create_table() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)