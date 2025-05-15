import pytest
from fixtures import mock_message, mock_router
from handlers.handlers import process_test_command, process_help_command
from aiogram.types import ReplyKeyboardMarkup

# Когда тест помечен @pytest.mark.asyncio, он становится сопрограммой (coroutine), вместе с ключевым словом await в теле
# pytest выполнит функцию теста как задачу asyncio, используя цикл событий, предоставляемый фикстурой event_loop
# https://habr.com/ru/companies/otus/articles/337108/

@pytest.mark.asyncio
async def test_process_test_command(mock_router, mock_message):
    # Вызываем хендлер
    await process_test_command(mock_message)

    assert mock_message.answer.called, "message.answer не был вызван"

    # Проверяем, что mock_ был вызван один раз с ожидаемым результатом
    mock_message.answer.assert_called_once_with(text="test!")


@pytest.mark.asyncio
async def test_process_help_command(mock_router, mock_message):
    # Вызываем хендлер
    await process_help_command(mock_message)

    assert mock_message.answer.called, "message.answer не был вызван"

    called_args, called_kwargs = mock_message.answer.call_args
    # print(called_kwargs)

    assert called_kwargs ["text"] == "хелп!"
    markup = called_kwargs["reply_markup"]
    assert isinstance(markup, ReplyKeyboardMarkup), "reply_markup не являеться inline-keyboard"
    # Проверяем, что mock_ был вызван один раз с ожидаемым результатом
    # mock_message.answer.assert_called_once_with(text="хелп!")



