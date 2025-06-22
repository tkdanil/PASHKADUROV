from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    """Модель пользователя Telegram."""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    username = Column(String)

    # Данные для подключения к виртуальной машине
    vm_ip = Column(String, nullable=True)
    vm_username = Column(String, nullable=True)
    vm_password = Column(String, nullable=True)


def create_db_tables(engine):
    """Создает таблицы в базе данных."""
    Base.metadata.create_all(engine)