__all__ = [
    "User",
    "VMConnection",
    "Base",
]

# Про ORM-паттерн асинхронного sqlalchemy и модели
# https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html#synopsis-orm

# декларативная модель базы данных python
# https://metanit.com/python/database/3.2.php
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, DATE, Integer, VARCHAR, Text, ForeignKey
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

class VMConnection(Base):
    __tablename__ = "vm_connections"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user_table.user_id"), nullable=False)
    ip_address = Column(VARCHAR(45), nullable=False)  # IPv4/IPv6
    username = Column(VARCHAR(255), nullable=False)
    password = Column(Text, nullable=False)
    created_at = Column(DATE, default=datetime.now)
