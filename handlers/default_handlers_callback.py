import time
from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.types import CallbackQuery
from aiogram.fsm.state import default_state

from keyboards import kb_start
from dict.lexicon_ru import lexicon, user_db


router = Router()

@router.callback_query(F.data == "cancel", StateFilter(default_state))
async def process_cancel_callback(callback: CallbackQuery):
    user_db[callback.from_user.id] = 1
    await callback.message.edit_text(
        text=lexicon["cancel"],
        reply_markup=kb_start.keyboard
    )

@router.callback_query()
async def process_other_callback(callback: CallbackQuery):
    await callback.answer(
        text=lexicon["other_callback"],
        show_alert=True
    )