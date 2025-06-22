#!/usr/bin/env python3
"""
Setup script for Telegram Bot for VM File Checking
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(command, description):
    """Выполнить команду с выводом описания"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} - успешно")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - ошибка:")
        print(f"   {e.stderr}")
        return False

def main():
    print("🚀 Настройка Telegram Bot для проверки файлов ВМ")
    print("=" * 50)
    
    # Проверяем Python
    python_version = sys.version_info
    if python_version < (3, 8):
        print(f"❌ Требуется Python 3.8+, у вас {python_version.major}.{python_version.minor}")
        return False
    
    print(f"✅ Python {python_version.major}.{python_version.minor}.{python_version.micro} - OK")
    
    # Создаем папку instance
    instance_dir = Path("instance")
    if not instance_dir.exists():
        print("📁 Создаем папку instance...")
        instance_dir.mkdir()
        print("✅ Папка instance создана")
    
    # Создаем виртуальное окружение
    venv_dir = Path("venv")
    if not venv_dir.exists():
        if not run_command("python -m venv venv", "Создание виртуального окружения"):
            return False
    
    # Активируем виртуальное окружение и устанавливаем зависимости
    if os.name == 'nt':  # Windows
        activate_script = "venv\\Scripts\\activate"
        pip_path = "venv\\Scripts\\pip"
    else:  # Unix/Linux/Mac
        activate_script = "venv/bin/activate"
        pip_path = "venv/bin/pip"
    
    # Устанавливаем зависимости
    if not run_command(f"{pip_path} install -r requirements.txt", "Установка зависимостей"):
        return False
    
    print("\n🎉 Настройка завершена!")
    print("\n📋 Для запуска бота:")
    print("   Windows: py main.py")
    print("   Linux/Mac: python3 main.py")
    print("   Или используйте: run.bat (Windows) / run.sh (Linux/Mac)")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1) 