from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from utils.ssh_client import SSHClient
from db.models import User
import paramiko


class BotLogic:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def register_user(self, telegram_id: int, username: str) -> str:
        user = await self.session.scalar(select(User).where(User.telegram_id == telegram_id))
        if user:
            return "Вы уже зарегистрированы!"
        self.session.add(User(telegram_id=telegram_id, username=username))
        await self.session.commit()
        return f"Привет, {username}! Вы зарегистрированы."

    async def get_user_status(self, telegram_id: int) -> str:
        user = await self.session.scalar(select(User).where(User.telegram_id == telegram_id))
        if not user:
            return "Вы не зарегистрированы. Используйте /start."
        status = f"Пользователь: {user.username}\n"
        if user.vm_ip and user.vm_username:
            status += f"ВМ: {user.vm_ip} (пользователь: {user.vm_username})"
        else:
            status += "ВМ не настроена. Используйте /vmpath."
        return status

    async def save_vm_path(self, telegram_id: int, ip: str, username: str, password: str) -> str:
        user = await self.session.scalar(select(User).where(User.telegram_id == telegram_id))
        if not user:
            return "Сначала зарегистрируйтесь через /start."
        user.vm_ip = ip
        user.vm_username = username
        user.vm_password = password
        await self.session.commit()
        return f"Данные для ВМ сохранены: {ip}, пользователь: {username}"

    async def check_vm_connection(self, telegram_id: int) -> str:
        """Проверка подключения к ВМ с детальной обработкой ошибок."""
        user = await self.session.scalar(select(User).where(User.telegram_id == telegram_id))
        if not user or not all([user.vm_ip, user.vm_username, user.vm_password]):
            return "Сначала укажите адрес ВМ через /vmpath."

        try:
            with SSHClient(user.vm_ip, user.vm_username, user.vm_password) as ssh:
                return "✅ Подключение к ВМ успешно!"
        except paramiko.AuthenticationException:
            return "❌ Ошибка аутентификации: Неверный логин или пароль."
        except paramiko.SSHException as e:
            return f"❌ Проблема с SSH: {e}. Возможно, на сервере отключена аутентификация по паролю."
        except TimeoutError:
            return f"❌ Ошибка: Не удалось подключиться к {user.vm_ip} за 10 секунд (timeout)."
        except Exception as e:
            return f"❌ Ошибка подключения: {e}. Проверьте IP-адрес и доступность сервера."

    async def list_home_dir(self, telegram_id: int) -> str:
        """Вывод содержимого домашнего каталога с детальной обработкой ошибок."""
        user = await self.session.scalar(select(User).where(User.telegram_id == telegram_id))
        if not user or not all([user.vm_ip, user.vm_username, user.vm_password]):
            return "Сначала укажите адрес ВМ через /vmpath."

        try:
            with SSHClient(user.vm_ip, user.vm_username, user.vm_password) as ssh:
                out, err = ssh.exec_command('ls -la ~')
                if err:
                    return f"⚠️ Команда выполнена с ошибкой: {err}"
                return f"📁 Содержимое домашнего каталога:\n```\n{out}\n```"
        except Exception as e:
            return f"❌ Ошибка: {e}"

    async def cat_text_files(self, telegram_id: int) -> str:
        """Вывод содержимого текстовых файлов с детальной обработкой ошибок."""
        user = await self.session.scalar(select(User).where(User.telegram_id == telegram_id))
        if not user or not all([user.vm_ip, user.vm_username, user.vm_password]):
            return "Сначала укажите адрес ВМ через /vmpath."

        try:
            with SSHClient(user.vm_ip, user.vm_username, user.vm_password) as ssh:
                find_cmd = "find ~ -maxdepth 1 -type f -name '*.txt'"
                out, err = ssh.exec_command(find_cmd)
                if err:
                    return f"⚠️ Ошибка поиска файлов: {err}"
                files = [f.strip() for f in out.splitlines() if f.strip()]
                if not files:
                    return "📄 Текстовые файлы (.txt) в домашней директории не найдены."
                result = []
                for file in files:
                    file_out, file_err = ssh.exec_command(f'cat "{file}"')
                    if file_err:
                        result.append(f"\n--- 📄 {file} (ошибка чтения) ---\n{file_err}")
                    else:
                        result.append(f"\n--- 📄 {file} ---\n{file_out}")
                return "📄 Содержимое текстовых файлов:\n" + "".join(result)
        except Exception as e:
            return f"❌ Ошибка: {e}"