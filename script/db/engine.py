from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine, async_sessionmaker, AsyncSession
from config import DB_NAME

def create_async_engine():
    return _create_async_engine(f"sqlite+aiosqlite:///{DB_NAME}")

def get_session_maker(engine):
    return async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)