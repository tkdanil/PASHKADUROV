@echo off
echo Starting Telegram Bot for VM File Checking...
echo.

REM Проверяем наличие Python (пробуем разные команды)
python --version >nul 2>&1
if not errorlevel 1 (
    set PYTHON_CMD=python
    goto :python_found
)

py --version >nul 2>&1
if not errorlevel 1 (
    set PYTHON_CMD=py
    goto :python_found
)

python3 --version >nul 2>&1
if not errorlevel 1 (
    set PYTHON_CMD=python3
    goto :python_found
)

echo Error: Python not found. Please install Python 3.8+
echo Try: https://www.python.org/downloads/
pause
exit /b 1

:python_found
echo Found Python: %PYTHON_CMD%
%PYTHON_CMD% --version

REM Создаем папку instance если её нет
if not exist "instance" (
    echo Creating instance directory...
    mkdir instance
)

REM Создаем виртуальное окружение если его нет
if not exist "venv" (
    echo Creating virtual environment...
    %PYTHON_CMD% -m venv venv
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
%PYTHON_CMD% main.py

pause 