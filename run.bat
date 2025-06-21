@echo off
echo Starting Telegram Bot for VM File Checking...
echo.

REM Проверяем наличие Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python not found. Please install Python 3.8+
    pause
    exit /b 1
)

REM Создаем папку instance если её нет
if not exist "instance" (
    echo Creating instance directory...
    mkdir instance
)

REM Устанавливаем зависимости если нужно
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Running tests...
python test_bot.py

echo.
echo Starting bot...
python main.py

pause 