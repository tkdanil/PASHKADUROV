__all__ = [
    "User",
    "Base",
]

# Про ORM-паттерн асинхронного sqlalchemy и модели
# https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html#synopsis-orm

# декларативная модель базы данных python
# https://metanit.com/python/database/3.2.php
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, DATE, Integer, VARCHAR, Text
from datetime import datetime

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_table"
    user_id = Column(Integer, primary_key=True)
    username =  Column(VARCHAR(255), unique=False, nullable=False)
    tutorcode = Column(VARCHAR(6),unique=False)
    subscribe = Column(VARCHAR(6), unique=False)
    extra = Column(Text, unique=False)
