from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

append_button = InlineKeyboardButton(
    text="Добавить строчки", callback_data="append_text"
)

delete_button = InlineKeyboardButton(
    text="Удалить строчки",
    callback_data="delete"
)

open_button = InlineKeyboardButton(text="Открыть список", callback_data="open_file")

keyboard = InlineKeyboardMarkup(inline_keyboard=[[open_button], [delete_button, append_button]])
