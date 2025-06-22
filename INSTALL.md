## Установка

### 1. Клонирование проекта
```bash
git clone <repository-url>
cd PASHKADUROV-1-1
```

### 2. Создание виртуального окружения (рекомендуется)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 4. Создание папки для базы данных
```bash
mkdir instance
```

## Проверка установки

Запустите тестовый скрипт для проверки всех компонентов:

```bash
python test_bot.py
```

Если все тесты пройдены успешно, вы увидите:
```
🎉 Все тесты пройдены! Бот готов к запуску.
```

## Запуск бота

### Простой запуск
```bash
python main.py
```

### Запуск в фоновом режиме (Linux/Mac)
```bash
nohup python main.py > bot.log 2>&1 &
```

### Запуск через systemd (Linux)
Создайте файл `/etc/systemd/system/telegram-bot.service`:

```ini
[Unit]
Description=Telegram Bot for VM File Checking
After=network.target

[Service]
Type=simple
User=your-username
WorkingDirectory=/path/to/PASHKADUROV-1-1
ExecStart=/path/to/python main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Затем:
```bash
sudo systemctl enable telegram-bot
sudo systemctl start telegram-bot
sudo systemctl status telegram-bot
```

## Использование бота

### 1. Начальная настройка
Отправьте боту команду `/start` для регистрации.

### 2. Настройка подключения к ВМ
Отправьте данные в формате:
```
/vmpath 192.168.1.100:ubuntu:mypassword
```

### 3. Проверка подключения
```
/check
```

### 4. Работа с файлами
```
/ls - список файлов
/cat - содержимое текстовых файлов
```

## Устранение неполадок

### Проблема: "ModuleNotFoundError"
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### Проблема: "Microsoft Visual C++ 14.0 or greater is required"
Установите Microsoft Visual C++ Build Tools:
https://visualstudio.microsoft.com/visual-cpp-build-tools/

### Проблема: "Permission denied" при подключении к SSH
1. Проверьте правильность IP адреса, логина и пароля
2. Убедитесь, что SSH сервер запущен на ВМ
3. Проверьте настройки файрвола

### Проблема: "Database is locked"
Убедитесь, что только один экземпляр бота запущен одновременно.

## Логирование

Бот выводит логи в консоль. Для сохранения логов в файл:

```bash
python main.py > bot.log 2>&1
```

## Обновление

1. Остановите бота
2. Обновите код: `git pull`
3. Установите новые зависимости: `pip install -r requirements.txt`
4. Запустите бота заново

## Безопасность

⚠️ **Важно**: 
- Пароли хранятся в базе данных в открытом виде
- В продакшене рекомендуется шифровать пароли
- Используйте бота только в доверенной сети
- Регулярно обновляйте зависимости

## Поддержка

При возникновении проблем:
1. Проверьте логи бота
2. Убедитесь, что все зависимости установлены
3. Проверьте подключение к интернету
4. Убедитесь, что токен бота корректный 