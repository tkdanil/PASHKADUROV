# План разбивки проекта на коммиты для 4 человек

## Общая информация
**Проект:** Telegram Bot для проверки содержимого файлов на виртуальных машинах  
**Команда:** 4 человека  
**Цель:** Показать поэтапную разработку проекта с логичными коммитами

---

## 🎯 Рекомендуемая последовательность коммитов

### **Человек 1: Основная архитектура и база данных**
**Роль:** Архитектор проекта

#### Коммит 1: "Initial project structure and database setup"
- Создание структуры проекта
- Настройка `requirements.txt`
- Создание `config.py` с базовой конфигурацией
- Создание папок: `db/`, `handlers/`, `utils/`, `tests/`

#### Коммит 2: "Database models and engine setup"
- Создание `db/models.py` с моделями User и VMConnection
- Создание `db/engine.py` для асинхронного подключения
- Создание `db/__init__.py` с функцией создания таблиц

#### Коммит 3: "Basic configuration and environment setup"
- Доработка `config.py` с токеном бота
- Создание `.env` файла (в .gitignore)
- Создание `main.py` с базовой структурой

---

### **Человек 2: SSH клиент и утилиты**
**Роль:** Backend разработчик

#### Коммит 4: "SSH client implementation"
- Создание `utils/ssh_client.py` с базовым SSH подключением
- Реализация функций подключения к VM
- Обработка ошибок подключения

#### Коммит 5: "File operations and command execution"
- Добавление функций выполнения команд на VM
- Реализация чтения файлов (`ls`, `cat`)
- Обработка различных форматов файлов

#### Коммит 6: "Error handling and logging improvements"
- Создание `utils/logging.py`
- Улучшение обработки ошибок SSH
- Добавление таймаутов и retry логики

---

### **Человек 3: Telegram бот команды и обработчики**
**Роль:** Frontend разработчик (Telegram API)

#### Коммит 7: "Basic bot commands structure"
- Создание `handlers/__init__.py`
- Создание `handlers/bot_commands.py` с командами
- Создание `handlers/keyboard.py` для клавиатур

#### Коммит 8: "User registration and status commands"
- Реализация `/start` команды
- Реализация `/status` команды
- Создание системы ролей (преподаватель/студент)

#### Коммит 9: "VM configuration commands"
- Реализация `/vmpath` команды
- Валидация формата IP:user:password
- Сохранение настроек в базу данных

---

### **Человек 4: Функциональность и тестирование**
**Роль:** QA и финальная интеграция

#### Коммит 10: "File checking functionality"
- Реализация `/check` команды для тестирования SSH
- Реализация `/ls` команды для просмотра файлов
- Реализация `/cat` команды для чтения файлов

#### Коммит 11: "Advanced features and improvements"
- Добавление поддержки больших файлов
- Разбивка длинных сообщений
- Улучшение UX с inline клавиатурами

#### Коммит 12: "Testing and documentation"
- Создание `tests/` папки с тестами
- Создание `README.md` с документацией
- Создание `INSTALL.md` с инструкциями по установке

---

## 📋 Детальные инструкции для каждого участника

### **Для Человека 1 (Архитектор):**

```bash
# Коммит 1: Структура проекта
git add .gitignore requirements.txt config.py
git commit -m "Initial project structure and database setup

- Created project folder structure
- Added requirements.txt with dependencies
- Created basic config.py
- Set up initial project architecture"

# Коммит 2: База данных
git add db/
git commit -m "Database models and engine setup

- Created User and VMConnection models
- Implemented async SQLAlchemy engine
- Added database initialization functions
- Set up SQLite database configuration"

# Коммит 3: Конфигурация
git add main.py .env.example
git commit -m "Basic configuration and environment setup

- Created main.py with bot initialization
- Added environment variable support
- Configured bot token handling
- Set up basic logging configuration"
```

### **Для Человека 2 (Backend):**

```bash
# Коммит 4: SSH клиент
git add utils/ssh_client.py
git commit -m "SSH client implementation

- Implemented Paramiko SSH client wrapper
- Added connection management functions
- Created async SSH operations
- Added basic error handling"

# Коммит 5: Операции с файлами
git add utils/ssh_client.py
git commit -m "File operations and command execution

- Added ls command implementation
- Added cat command for text files
- Implemented file format detection
- Added command execution utilities"

# Коммит 6: Обработка ошибок
git add utils/logging.py
git commit -m "Error handling and logging improvements

- Created centralized logging system
- Improved SSH error handling
- Added connection timeouts
- Implemented retry logic for failed connections"
```

### **Для Человека 3 (Frontend):**

```bash
# Коммит 7: Структура команд
git add handlers/
git commit -m "Basic bot commands structure

- Created handlers package structure
- Defined bot commands list
- Created keyboard layouts
- Set up command registration system"

# Коммит 8: Регистрация пользователей
git add handlers/handlers.py
git commit -m "User registration and status commands

- Implemented /start command with user registration
- Added /status command to show user info
- Created role-based user system
- Added user state management"

# Коммит 9: Настройка VM
git add handlers/handlers.py
git commit -m "VM configuration commands

- Implemented /vmpath command for VM setup
- Added input validation for IP:user:password format
- Created database storage for VM connections
- Added connection parameter validation"
```

### **Для Человека 4 (QA/Интеграция):**

```bash
# Коммит 10: Функциональность проверки
git add handlers/handlers.py
git commit -m "File checking functionality

- Implemented /check command for SSH testing
- Added /ls command for file listing
- Created /cat command for file reading
- Added support for multiple text file formats"

# Коммит 11: Улучшения
git add handlers/handlers.py utils/ssh_client.py
git commit -m "Advanced features and improvements

- Added large file handling with message splitting
- Implemented inline keyboards for better UX
- Added file size limits and pagination
- Improved error messages and user feedback"

# Коммит 12: Тестирование и документация
git add tests/ README.md INSTALL.md
git commit -m "Testing and documentation

- Created comprehensive test suite
- Added detailed README with usage examples
- Created installation instructions
- Added project documentation and examples"
```

---

## 🎯 Рекомендации по организации работы

### **Временные рамки:**
- **Человек 1:** Дни 1-2 (архитектура)
- **Человек 2:** Дни 2-3 (SSH функциональность)
- **Человек 3:** Дни 3-4 (Telegram команды)
- **Человек 4:** Дни 4-5 (тестирование и финализация)

### **Порядок работы:**
1. **Человек 1** начинает первым и создает основу
2. **Человек 2** подключается после создания структуры БД
3. **Человек 3** начинает после готовности SSH клиента
4. **Человек 4** интегрирует все компоненты и тестирует

### **Советы по коммитам:**
- Каждый коммит должен быть **логически завершенным**
- Используйте **описательные сообщения** коммитов
- Включайте **списки изменений** в сообщения коммитов
- Делайте коммиты **регулярно** (не накапливайте изменения)

### **Финальная подготовка:**
- Все участники должны **протестировать** финальную версию
- Убедиться, что **все команды работают**
- Проверить **документацию** на актуальность
- Подготовить **презентацию** проекта

---

## 📊 Ожидаемый результат

После выполнения этого плана у вас будет:
- ✅ **12 логичных коммитов** с четким разделением ответственности
- ✅ **4 участника** с равномерным вкладом в проект
- ✅ **Полнофункциональный бот** с документацией
- ✅ **Готовый к сдаче проект** с понятной историей разработки

Этот план покажет преподавателю, что команда работала **организованно** и **поэтапно**, а не создавала проект за один день. 