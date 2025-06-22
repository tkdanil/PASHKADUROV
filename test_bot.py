#!/usr/bin/env python3
"""
Тестовый файл для проверки функциональности Telegram бота
"""

import asyncio
import sys
import os

# Добавляем текущую директорию в путь
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

async def test_imports():
    """Тестируем импорты всех модулей"""
    try:
        print("Тестируем импорты...")
        
        # Тестируем основные зависимости
        import paramiko
        print("✅ Paramiko импортирован успешно")
        
        import aiogram
        print("✅ Aiogram импортирован успешно")
        
        import sqlalchemy
        print("✅ SQLAlchemy импортирован успешно")
        
        import aiosqlite
        print("✅ Aiosqlite импортирован успешно")
        
        # Тестируем наши модули
        from config import TOKEN
        print(f"✅ Конфигурация загружена, токен: {TOKEN[:10]}...")
        
        from script.db import User, VMConnection, Base
        print("✅ Модели базы данных импортированы")
        
        from utils.ssh_client import SSHClient
        print("✅ SSH клиент импортирован")
        
        from handlers.handlers import register_message_handlers
        print("✅ Обработчики импортированы")
        
        print("\n🎉 Все импорты прошли успешно!")
        return True
        
    except Exception as e:
        print(f"❌ Ошибка импорта: {e}")
        return False

async def test_database():
    """Тестируем базу данных"""
    try:
        print("\nТестируем базу данных...")
        
        from script.db import async_session, async_create_table
        from script.db import User, VMConnection
        
        # Создаем таблицы
        await async_create_table()
        print("✅ Таблицы созданы успешно")
        
        # Тестируем сессию
        async with async_session() as session:
            print("✅ Сессия базы данных работает")
        
        print("🎉 База данных работает корректно!")
        return True
        
    except Exception as e:
        print(f"❌ Ошибка базы данных: {e}")
        return False

async def test_ssh_client():
    """Тестируем SSH клиент"""
    try:
        print("\nТестируем SSH клиент...")
        
        from utils.ssh_client import SSHClient
        
        client = SSHClient()
        print("✅ SSH клиент создан")
        
        # Тестируем отключение (без подключения)
        client.disconnect()
        print("✅ SSH клиент корректно отключается")
        
        print("🎉 SSH клиент работает корректно!")
        return True
        
    except Exception as e:
        print(f"❌ Ошибка SSH клиента: {e}")
        return False

async def main():
    """Основная функция тестирования"""
    print("🚀 Запуск тестирования Telegram бота...\n")
    
    tests = [
        test_imports(),
        test_database(),
        test_ssh_client()
    ]
    
    results = await asyncio.gather(*tests, return_exceptions=True)
    
    print("\n" + "="*50)
    print("РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ:")
    print("="*50)
    
    passed = 0
    total = len(results)
    
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"❌ Тест {i+1} провален: {result}")
        elif result:
            print(f"✅ Тест {i+1} пройден")
            passed += 1
        else:
            print(f"❌ Тест {i+1} провален")
    
    print(f"\n📊 Результат: {passed}/{total} тестов пройдено")
    
    if passed == total:
        print("🎉 Все тесты пройдены! Бот готов к запуску.")
        print("\nДля запуска бота выполните:")
        print("python main.py")
    else:
        print("⚠️  Некоторые тесты провалены. Проверьте зависимости.")

if __name__ == "__main__":
    asyncio.run(main()) 