__all__ = [
    'register_message_handlers'
]


# Работа c Router - https://docs.aiogram.dev/en/v3.14.0/dispatcher/router.html
# Пример работы с Router через декораторы @router - https://mastergroosha.github.io/aiogram-3-guide/routers/
# Пример работы с Router через функцию сборщик https://stackoverflow.com/questions/77809738/how-to-connect-a-router-in-aiogram-3-x-x#:~:text=1-,Answer,-Sorted%20by%3A


from aiogram import types, Router, filters, F
from .keyboard import keyboard_continue, keyboard_start  # импорт из клавиатур
from .callbacks import callback_message, callback_start_tutor, start_student, callback_insert_tutorcode  # импорт из коллбека
from db import async_session, User, VMConnection
from sqlalchemy import select
from utils.ssh_client import SSHClient
import re


# информации о статусе
status_string: str = """
UserId {}
UserName {}
"""

async def command_start_handler(message: types.Message):
    async with async_session() as session:
        query = select(User).where(message.from_user.id == User.user_id)
        result = await session.execute(query)
        if result.scalars().all():
            info="чтобы продолжить, вызовите команду /status"
            await message.answer(info)
        else:
            await  message.answer("выберите роль", reply_markup=keyboard_start)


async def command_status_handler(message: types.Message):
    async with async_session() as session:
        query = select(User).where(message.from_user.id == User.user_id)
        result = await session.execute(query)
        user = result.scalar()
        
        if not user:
            await message.answer("Пользователь не найден. Используйте /start для регистрации.")
            return
            
        if user.tutorcode:
            info = status_string + "Код преподавателя: {}"
            info = info.format(user.user_id, user.username, user.tutorcode)

        if user.subscribe:
            code = str(user.subscribe)
            info = status_string + "Преподаватель: {}"
            query = select(User).where(code == User.tutorcode)
            result = await session.execute(query)
            tutor = result.scalar()
            try:
                info = info.format(user.user_id, user.username, tutor.username)
            except:
                info = info.format(user.user_id, user.username)
        
        # Проверяем наличие настроек ВМ
        vm_query = select(VMConnection).where(VMConnection.user_id == message.from_user.id)
        vm_result = await session.execute(vm_query)
        vm_connection = vm_result.scalar()
        
        if vm_connection:
            info += f"\n\nНастроена ВМ: {vm_connection.ip_address}"
            info += f"\nПользователь ВМ: {vm_connection.username}"
        else:
            info += "\n\nДля работы с виртуальной машиной используйте команду /vmpath"
            
        await message.answer(info)


async def command_vmpath_handler(message: types.Message):
    """Обработчик команды /vmpath для настройки подключения к ВМ"""
    # Ожидаем формат: IP:пользователь:пароль
    text = message.text.strip()
    
    if text == "/vmpath":
        await message.answer(
            "Для настройки подключения к виртуальной машине отправьте данные в формате:\n"
            "IP:пользователь:пароль\n\n"
            "Например: 192.168.1.100:ubuntu:mypassword"
        )
        return
    
    # Парсим данные подключения
    try:
        # Убираем команду если она есть
        if text.startswith("/vmpath "):
            text = text[8:]
        
        parts = text.split(":")
        if len(parts) != 3:
            await message.answer(
                "Неверный формат. Используйте: IP:пользователь:пароль\n"
                "Например: 192.168.1.100:ubuntu:mypassword"
            )
            return
        
        ip_address, username, password = parts
        
        # Проверяем IP адрес
        if not re.match(r'^(\d{1,3}\.){3}\d{1,3}$', ip_address):
            await message.answer("Неверный формат IP адреса")
            return
        
        # Сохраняем в базу данных
        async with async_session() as session:
            # Проверяем существующее подключение
            existing_query = select(VMConnection).where(VMConnection.user_id == message.from_user.id)
            existing_result = await session.execute(existing_query)
            existing_connection = existing_result.scalar()
            
            if existing_connection:
                # Обновляем существующее подключение
                existing_connection.ip_address = ip_address
                existing_connection.username = username
                existing_connection.password = password
            else:
                # Создаем новое подключение
                new_connection = VMConnection(
                    user_id=message.from_user.id,
                    ip_address=ip_address,
                    username=username,
                    password=password
                )
                session.add(new_connection)
            
            await session.commit()
        
        await message.answer(
            f"Настройки ВМ сохранены:\n"
            f"IP: {ip_address}\n"
            f"Пользователь: {username}\n\n"
            f"Используйте /check для проверки подключения"
        )
        
    except Exception as e:
        await message.answer(f"Ошибка при сохранении настроек: {str(e)}")


async def command_check_handler(message: types.Message):
    """Обработчик команды /check для проверки подключения к ВМ"""
    async with async_session() as session:
        # Получаем настройки ВМ
        vm_query = select(VMConnection).where(VMConnection.user_id == message.from_user.id)
        vm_result = await session.execute(vm_query)
        vm_connection = vm_result.scalar()
        
        if not vm_connection:
            await message.answer(
                "Настройки ВМ не найдены. Используйте /vmpath для настройки подключения."
            )
            return
        
        await message.answer("Проверяю подключение к ВМ...")
        
        # Тестируем подключение
        ssh_client = SSHClient()
        try:
            success = await ssh_client.connect(
                vm_connection.ip_address,
                vm_connection.username,
                vm_connection.password
            )
            
            if success:
                await message.answer("✅ Подключение к ВМ успешно установлено!")
            else:
                await message.answer("❌ Не удалось подключиться к ВМ. Проверьте настройки.")
                
        except Exception as e:
            await message.answer(f"❌ Ошибка подключения: {str(e)}")
        finally:
            ssh_client.disconnect()


async def command_ls_handler(message: types.Message):
    """Обработчик команды /ls для просмотра файлов в домашнем каталоге"""
    async with async_session() as session:
        # Получаем настройки ВМ
        vm_query = select(VMConnection).where(VMConnection.user_id == message.from_user.id)
        vm_result = await session.execute(vm_query)
        vm_connection = vm_result.scalar()
        
        if not vm_connection:
            await message.answer(
                "Настройки ВМ не найдены. Используйте /vmpath для настройки подключения."
            )
            return
        
        await message.answer("Получаю список файлов...")
        
        # Подключаемся и получаем список файлов
        ssh_client = SSHClient()
        try:
            success = await ssh_client.connect(
                vm_connection.ip_address,
                vm_connection.username,
                vm_connection.password
            )
            
            if not success:
                await message.answer("❌ Не удалось подключиться к ВМ")
                return
            
            success, files = await ssh_client.list_home_directory(vm_connection.username)
            
            if success and files:
                # Разбиваем на части если файлов много
                file_list = "\n".join(files)
                if len(file_list) > 4096:
                    # Разбиваем на части
                    parts = [file_list[i:i+4096] for i in range(0, len(file_list), 4096)]
                    for i, part in enumerate(parts):
                        await message.answer(f"Часть {i+1}:\n```\n{part}\n```", parse_mode="Markdown")
                else:
                    await message.answer(f"```\n{file_list}\n```", parse_mode="Markdown")
            else:
                await message.answer("Не удалось получить список файлов или каталог пуст")
                
        except Exception as e:
            await message.answer(f"❌ Ошибка: {str(e)}")
        finally:
            ssh_client.disconnect()


async def command_cat_handler(message: types.Message):
    """Обработчик команды /cat для просмотра содержимого текстовых файлов"""
    async with async_session() as session:
        # Получаем настройки ВМ
        vm_query = select(VMConnection).where(VMConnection.user_id == message.from_user.id)
        vm_result = await session.execute(vm_query)
        vm_connection = vm_result.scalar()
        
        if not vm_connection:
            await message.answer(
                "Настройки ВМ не найдены. Используйте /vmpath для настройки подключения."
            )
            return
        
        await message.answer("Читаю содержимое текстовых файлов...")
        
        # Подключаемся и читаем файлы
        ssh_client = SSHClient()
        try:
            success = await ssh_client.connect(
                vm_connection.ip_address,
                vm_connection.username,
                vm_connection.password
            )
            
            if not success:
                await message.answer("❌ Не удалось подключиться к ВМ")
                return
            
            success, content = await ssh_client.read_text_files(vm_connection.username)
            
            if success:
                if len(content) > 4096:
                    # Разбиваем на части
                    parts = [content[i:i+4096] for i in range(0, len(content), 4096)]
                    for i, part in enumerate(parts):
                        await message.answer(f"Часть {i+1}:\n```\n{part}\n```", parse_mode="Markdown")
                else:
                    await message.answer(f"```\n{content}\n```", parse_mode="Markdown")
            else:
                await message.answer(f"❌ Ошибка чтения файлов: {content}")
                
        except Exception as e:
            await message.answer(f"❌ Ошибка: {str(e)}")
        finally:
            ssh_client.disconnect()


async def command_help_handler(message: types.Message):
    """Команда help"""
    help_text = """
🤖 **Доступные команды:**

/start - Регистрация нового пользователя
/status - Информация о пользователе и настройках ВМ
/vmpath - Настройка подключения к виртуальной машине
/check - Проверка подключения к ВМ
/ls - Список файлов в домашнем каталоге
/cat - Содержимое всех текстовых файлов

📝 **Формат настройки ВМ:**
IP:пользователь:пароль
Пример: 192.168.1.100:ubuntu:mypassword
"""
    await message.answer(help_text, parse_mode="Markdown")


# Здесь описывается маршрутизация
async def register_message_handlers(router: Router):
    """Маршрутизация обработчиков"""
    router.message.register(command_start_handler, filters.Command(commands=["start"]))
    router.message.register(command_status_handler, filters.Command(commands=["status"]))
    router.message.register(command_vmpath_handler, filters.Command(commands=["vmpath"]))
    router.message.register(command_check_handler, filters.Command(commands=["check"]))
    router.message.register(command_ls_handler, filters.Command(commands=["ls"]))
    router.message.register(command_cat_handler, filters.Command(commands=["cat"]))
    router.message.register(command_help_handler, filters.Command(commands=["help"]))
    router.callback_query.register(callback_message, F.data.endswith("_continue"))
    router.callback_query.register(callback_start_tutor, F.data.endswith("_tutor"))
    router.callback_query.register(callback_insert_tutorcode, F.data.endswith("_student"))
    router.message.register(start_student, F.text.startswith("tutorcode-"))

