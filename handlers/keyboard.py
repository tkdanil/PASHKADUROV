


# TODO - создайте клавиатуру, которая будет появляться в сообщении либо находится там постоянно
# Статичная клавиатура ReplyKeyboardMarkup https://docs.aiogram.dev/en/v3.15.0/api/types/reply_keyboard_markup.html
# Динамически генерируемая клавиатура Keyboard builder https://docs.aiogram.dev/en/v3.15.0/utils/keyboard.html
# Примеры создания клавиатуры ReplyKeyboardMarkup https://habr.com/ru/articles/820733/#:~:text=%D0%98%D0%BC%D0%BF%D0%BE%D1%80%D1%82%D1%8B%20%D0%B2%20all_kb.py%3A
# Примеры создания клавиатуры Keyboard builder https://mastergroosha.github.io/aiogram-3-guide/buttons/

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
#подстрочная клавиатура
main_keyboard_list = [
        [KeyboardButton(text="Статус"), ],
    ]

main_keyboard = ReplyKeyboardMarkup(keyboard=main_keyboard_list, resize_keyboard=True, one_time_keyboard=True)


# Клавиатура в сообщении
button_continue = [
    [InlineKeyboardButton(text="ДАлее",callback_data="continue"),]
]
keyboard_continue = InlineKeyboardMarkup(inline_keyboard=button_continue)