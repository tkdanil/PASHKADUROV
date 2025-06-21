#!/bin/bash

echo "Starting Telegram Bot for VM File Checking..."
echo

# Проверяем наличие Python
if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 not found. Please install Python 3.8+"
    exit 1
fi

# Создаем папку instance если её нет
if [ ! -d "instance" ]; then
    echo "Creating instance directory..."
    mkdir -p instance
fi

# Создаем виртуальное окружение если его нет
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo
echo "Running tests..."
python test_bot.py

echo
echo "Starting bot..."
python main.py 