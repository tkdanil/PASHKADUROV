# Настройка проекта в VS Code

## Шаг 1: Открытие проекта

1. Запустите VS Code
2. Выберите `File` → `Open Folder` (или `Ctrl+K Ctrl+O`)
3. Выберите папку с проектом `PASHKADUROV-1-1`
4. Нажмите `Select Folder`

## Шаг 2: Установка расширений Python

### Обязательные расширения:
1. **Python** (от Microsoft) - основное расширение для Python
2. **Pylance** - улучшенный языковой сервер для Python
3. **Python Indent** - автоматические отступы

### Дополнительные расширения:
- **Python Docstring Generator** - генерация документации
- **Python Test Explorer** - для запуска тестов
- **GitLens** - улучшенная работа с Git

### Установка расширений:
1. Нажмите `Ctrl+Shift+X` для открытия панели расширений
2. Найдите "Python" и установите расширение от Microsoft
3. VS Code автоматически предложит установить Pylance

## Шаг 3: Настройка интерпретатора Python

### Автоматическая настройка:
1. Откройте любой `.py` файл в проекте
2. VS Code предложит выбрать интерпретатор Python
3. Нажмите `Ctrl+Shift+P` → введите "Python: Select Interpreter"
4. Выберите Python 3.8+ или создайте новое виртуальное окружение

### Ручная настройка:
1. Нажмите `Ctrl+Shift+P`
2. Введите "Python: Select Interpreter"
3. Выберите "Enter interpreter path..."
4. Укажите путь к Python или выберите "Find..."
5. Для создания виртуального окружения выберите "Create Environment..."

## Шаг 4: Создание виртуального окружения

### Способ 1: Через VS Code
1. Нажмите `Ctrl+Shift+P`
2. Введите "Python: Create Environment"
3. Выберите "Venv"
4. Выберите Python 3.8+
5. VS Code автоматически активирует окружение

### Способ 2: Через терминал
1. Откройте терминал: `Ctrl+`` (обратная кавычка)
2. Выполните:
```bash
python -m venv venv
```

## Шаг 5: Активация виртуального окружения

### В терминале VS Code:
**Windows:**
```bash
.\venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### Автоматическая активация:
VS Code автоматически активирует виртуальное окружение, если оно выбрано как интерпретатор.

## Шаг 6: Установка зависимостей

### Способ 1: Через терминал VS Code
1. Откройте терминал: `Ctrl+``
2. Убедитесь, что виртуальное окружение активировано (должно быть `(venv)` в начале строки)
3. Выполните:
```bash
pip install -r requirements.txt
```

### Способ 2: Автоматический скрипт
```bash
python setup.py
```

### Способ 3: Через Command Palette
1. Нажмите `Ctrl+Shift+P`
2. Введите "Python: Install Package"
3. Выберите "Install from requirements.txt"

## Шаг 7: Создание папки instance

В терминале VS Code выполните:
```bash
mkdir instance
```

## Шаг 8: Настройка запуска

### Создание конфигурации запуска:
1. Нажмите `F5` или перейдите в панель "Run and Debug" (`Ctrl+Shift+D`)
2. Выберите "create a launch.json file"
3. Выберите "Python"
4. Выберите "Python File"

### Настройка launch.json:
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}"
        },
        {
            "name": "Python: Main Bot",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/main.py",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}"
        }
    ]
}
```

## Шаг 9: Запуск бота

### Способ 1: Через F5
1. Откройте файл `main.py`
2. Нажмите `F5`
3. Выберите конфигурацию "Python: Main Bot"

### Способ 2: Через терминал
1. Откройте терминал: `Ctrl+``
2. Убедитесь, что виртуальное окружение активировано
3. Выполните:
```bash
python main.py
```

### Способ 3: Через Command Palette
1. Нажмите `Ctrl+Shift+P`
2. Введите "Python: Run Python File in Terminal"
3. Выберите файл `main.py`

## Шаг 10: Проверка работы

После запуска в терминале VS Code вы должны увидеть:
```
INFO:aiogram.dispatcher:Start polling
INFO:aiogram.dispatcher:Run polling for bot @PashadurovvBot id=7399928399 - 'Pashadurov'
```

## Остановка бота

- Нажмите `Ctrl+C` в терминале
- Или нажмите красную кнопку "Stop" в панели Debug

## Отладка

### Установка точек останова:
1. Кликните слева от номера строки в коде
2. Появится красная точка - точка останова
3. Запустите отладку через `F5`

### Переменные и стек вызовов:
- В панели Debug будут видны все переменные
- Можно просматривать значения в реальном времени

## Возможные проблемы

### Проблема: "No module named 'aiogram'"
**Решение:**
1. Убедитесь, что выбран правильный интерпретатор Python
2. Проверьте, что виртуальное окружение активировано
3. Переустановите зависимости: `pip install -r requirements.txt`

### Проблема: Неправильная рабочая директория
**Решение:**
1. В `launch.json` установите правильный `cwd`
2. Или запускайте через терминал из корня проекта

### Проблема: Терминал не активирует виртуальное окружение
**Решение:**
1. Нажмите `Ctrl+Shift+P` → "Python: Select Interpreter"
2. Выберите интерпретатор из папки `venv`
3. Перезапустите терминал: `Ctrl+Shift+P` → "Terminal: Create New Terminal"

### Проблема: IntelliSense не работает
**Решение:**
1. Убедитесь, что установлено расширение Pylance
2. Перезапустите VS Code
3. Проверьте, что выбран правильный интерпретатор

## Полезные настройки VS Code

### settings.json для Python проекта:
```json
{
    "python.defaultInterpreterPath": "./venv/Scripts/python.exe",
    "python.terminal.activateEnvironment": true,
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "python.analysis.autoImportCompletions": true
}
```

### Горячие клавиши:
- `F5` - запуск/отладка
- `Ctrl+F5` - запуск без отладки
- `Ctrl+`` - открыть/закрыть терминал
- `Ctrl+Shift+P` - Command Palette
- `Ctrl+Shift+X` - панель расширений

## Полезные советы

1. **Автодополнение:** VS Code с Pylance предоставляет отличное автодополнение
2. **Go to Definition:** `F12` - переход к определению функции/класса
3. **Find All References:** `Shift+F12` - найти все использования
4. **Rename Symbol:** `F2` - переименование переменных/функций
5. **Multi-cursor:** `Alt+Click` - множественные курсоры для редактирования
6. **Split Editor:** `Ctrl+\` - разделение редактора

## Структура проекта в VS Code

```
PASHKADUROV-1-1/
├── main.py              # Главный файл (запускайте его)
├── config.py            # Конфигурация
├── requirements.txt     # Зависимости
├── setup.py            # Автоматическая установка
├── INSTALL.md          # Подробная инструкция
├── VSCODE_SETUP.md     # Эта инструкция
├── .vscode/            # Настройки VS Code (создается автоматически)
│   ├── launch.json     # Конфигурации запуска
│   └── settings.json   # Настройки проекта
├── handlers/           # Обработчики команд
├── db/                 # База данных
├── utils/              # Утилиты
└── tests/              # Тесты
```

## Дополнительные расширения для разработки

- **GitLens** - улучшенная работа с Git
- **Thunder Client** - тестирование API
- **Error Lens** - показ ошибок прямо в коде
- **Bracket Pair Colorizer** - цветовая подсветка скобок
- **Auto Rename Tag** - автоматическое переименование тегов
- **Material Icon Theme** - красивые иконки для файлов 