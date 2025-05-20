
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup






button_continue = InlineKeyboardButton(text="ДАлее",callback_data="button_continue")

button_tutor = InlineKeyboardButton(text="Слушатель",callback_data="button_student")

button_student = InlineKeyboardButton(text="Преподаватель",callback_data="button_tutor")



keyboard_continue = InlineKeyboardMarkup(inline_keyboard=[
        [button_continue, ]
    ])

keyboard_start = InlineKeyboardMarkup(inline_keyboard=[
        [button_student, button_tutor ]
    ])