from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from dict.lexicon_ru import user_db
from keyboards.kb_cancel import cancel_button
from other_fuctions.other_fuctions import len_file

def create_pagination(id: int) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(InlineKeyboardButton(
        text="<<",
        callback_data="<<"
        ),
        InlineKeyboardButton(
            text=str(user_db[id])+"/"+str(abs(-len_file(id)//10)),
            callback_data="select_page"
        ),
        InlineKeyboardButton(
            text=">>",
            callback_data=">>"
        ))
    kb_builder.row(cancel_button)
    return kb_builder.as_markup()
