import pytest
from unittest.mock import AsyncMock
from aiogram import Router
from aiogram.types import Message
from aiogram import Router
# Фикстуры в pytest позволяют выносить в отдельные функции типовые действия
# например: настройка тестового окружения, создание тестовых данных, выполнение завершающие действия
# https://habr.com/ru/articles/731296/

@pytest.fixture
def mock_message():
    """Mock сообщение"""
    mock_msg = AsyncMock(spec=Message)
    mock_msg.answer =  AsyncMock()
    mock_msg.from_user = AsyncMock()
    mock_msg.from_user.id = AsyncMock
    mock_msg.from_username = AsyncMock
    return mock_msg


@pytest.fixture
def mock_router():
    """Mock router"""
    router = Router()
    return router
