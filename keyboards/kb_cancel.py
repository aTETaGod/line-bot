from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


cancel_button = InlineKeyboardButton(
    text="Вернуться назад",
    callback_data="cancel"
)

cancel_append_button = InlineKeyboardButton(
    text="Я больше не хочу добавлять строчки",
    callback_data="cancel_append"
)

cancel_delete_button = InlineKeyboardButton(
    text="Я больше не хочу удалять строчки",
    callback_data="cancel_delete"
)

keyboard_cancel = InlineKeyboardMarkup(inline_keyboard=[[cancel_button]])
keyboard_cancel_append = InlineKeyboardMarkup(inline_keyboard=[[cancel_append_button]])
keyboard_cancel_delete = InlineKeyboardMarkup(inline_keyboard=[[cancel_delete_button]])