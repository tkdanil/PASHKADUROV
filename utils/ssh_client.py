import paramiko
import asyncio
from typing import Optional, Tuple, List
import logging

logger = logging.getLogger(__name__)

class SSHClient:
    def __init__(self):
        self.client = None
    
    async def connect(self, hostname: str, username: str, password: str, port: int = 22) -> bool:
        """Асинхронное подключение к SSH серверу"""
        try:
            loop = asyncio.get_event_loop()
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            # Выполняем подключение в отдельном потоке
            await loop.run_in_executor(
                None, 
                lambda: self.client.connect(
                    hostname=hostname,
                    port=port,
                    username=username,
                    password=password,
                    timeout=10
                )
            )
            return True
        except Exception as e:
            logger.error(f"Ошибка подключения к SSH: {e}")
            return False
    
    async def execute_command(self, command: str) -> Tuple[bool, str, str]:
        """Выполнение команды на удаленном сервере"""
        if not self.client:
            return False, "", "Нет активного подключения"
        
        try:
            loop = asyncio.get_event_loop()
            stdin, stdout, stderr = await loop.run_in_executor(
                None, 
                self.client.exec_command, 
                command
            )
            
            # Читаем вывод
            output = await loop.run_in_executor(None, stdout.read)
            error = await loop.run_in_executor(None, stderr.read)
            
            return True, output.decode('utf-8'), error.decode('utf-8')
        except Exception as e:
            logger.error(f"Ошибка выполнения команды: {e}")
            return False, "", str(e)
    
    async def list_home_directory(self, username: str) -> Tuple[bool, List[str]]:
        """Получение списка файлов в домашнем каталоге"""
        success, output, error = await self.execute_command(f"ls -la /home/{username}")
        if success:
            files = [line.strip() for line in output.split('\n') if line.strip()]
            return True, files
        return False, []
    
    async def read_text_files(self, username: str) -> Tuple[bool, str]:
        """Чтение содержимого всех текстовых файлов в домашнем каталоге"""
        # Находим все текстовые файлы
        find_cmd = f"find /home/{username} -type f -name '*.txt' -o -name '*.log' -o -name '*.conf' -o -name '*.cfg' -o -name '*.ini' -o -name '*.md' -o -name '*.py' -o -name '*.sh' -o -name '*.json' -o -name '*.xml' -o -name '*.yml' -o -name '*.yaml'"
        
        success, output, error = await self.execute_command(find_cmd)
        if not success:
            return False, f"Ошибка поиска файлов: {error}"
        
        files = [line.strip() for line in output.split('\n') if line.strip()]
        if not files:
            return True, "Текстовые файлы не найдены"
        
        # Читаем содержимое каждого файла
        content = []
        for file_path in files:
            try:
                success, file_content, error = await self.execute_command(f"cat '{file_path}'")
                if success:
                    content.append(f"=== {file_path} ===\n{file_content}\n")
                else:
                    content.append(f"=== {file_path} ===\nОшибка чтения: {error}\n")
            except Exception as e:
                content.append(f"=== {file_path} ===\nОшибка: {str(e)}\n")
        
        return True, "\n".join(content)
    
    def disconnect(self):
        """Отключение от SSH сервера"""
        if self.client:
            self.client.close()
            self.client = None 