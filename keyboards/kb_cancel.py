from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.kb_start import append_button

cancel_button = InlineKeyboardButton(
    text="Вернуться назад",
    callback_data="cancel"
)

cancel_append_button = InlineKeyboardButton(
    text="Я больше не хочу добавлять строчки",
    callback_data="cancel_append"
)

keyboard_cancel_open = InlineKeyboardMarkup(inline_keyboard=[[append_button], [cancel_button]])
keyboard_cancel = InlineKeyboardMarkup(inline_keyboard=[[cancel_button]])
keyboard_cancel_append = InlineKeyboardMarkup(inline_keyboard=[[cancel_append_button]])