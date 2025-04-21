
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