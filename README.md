# PASHKADUROV
## Запуск проекта из исходника

1. Для запуска проекта стяните его с помощью git clone

2. Создайте изолированную среду. Например, .venv

Bash



python3 -m venv .venv


3. Запустите среду и установите зависимости
   
Bash



pip install -r requirements.txt


4. Полученный токен в [BotFather](https://t.me/BotFather) вставить в созданный файл .env

copy



TOKEN=<ВАШ ТОКЕН>


5. Для запуска проекта введите в консоли

Bash



python3 main.py
