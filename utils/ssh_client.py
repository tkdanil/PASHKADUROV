import paramiko
from typing import Tuple

class SSHClient:
    def __init__(self, ip: str, username: str, password: str):
        self.ip = ip
        self.username = username
        self.password = password
        self.client = None

    def connect(self):
        """
        Подключение к SSH серверу.
        Вызывает исключение в случае ошибки, вместо возврата False.
        """
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.ip, username=self.username, password=self.password, timeout=10)

    def exec_command(self, command: str) -> Tuple[str, str]:
        """Выполнение команды на сервере"""
        if not self.client:
            raise Exception("SSH client not connected")
        stdin, stdout, stderr = self.client.exec_command(command)
        out = stdout.read().decode(errors='ignore')
        err = stderr.read().decode(errors='ignore')
        return out, err

    def close(self):
        """Закрытие соединения"""
        if self.client:
            self.client.close()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()