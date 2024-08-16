import time
from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.types import CallbackQuery
from aiogram.fsm.state import default_state

from keyboards import kb_start
from keyboards.kb_cancel import keyboard_cancel
from dict.lexicon_ru import lexicon
from other_fuctions.other_fuctions import open_file

router = Router()

@router.callback_query(F.data == "open_file", StateFilter(default_state))
async def process_open_file_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=lexicon["open"]+open_file(callback.from_user.id),
        reply_markup=keyboard_cancel
    )


@router.callback_query(F.data == "cancel", StateFilter(default_state))
async def process_cancel_callback(callback: CallbackQuery):
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