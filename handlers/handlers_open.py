from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.types import CallbackQuery
from aiogram.fsm.state import default_state

from dict.lexicon_ru import lexicon, user_db
from filters.infinite_void import domain_expansion
from keyboards.kb_cancel import keyboard_cancel_open
from keyboards.kb_open import create_pagination
from other_fuctions.other_fuctions import len_file, open_file


router = Router()

@router.callback_query(domain_expansion(), F.data == "open_file", StateFilter(default_state))
async def process_open_file(callback: CallbackQuery):
     await callback.message.edit_text(
          text=open_file(callback.from_user.id, 1),
          reply_markup=keyboard_cancel_open
          )

@router.callback_query(F.data == "open_file", StateFilter(default_state))
async def process_open_file_press(callback: CallbackQuery):
     await callback.message.edit_text(
          text=lexicon["open"]+open_file(callback.from_user.id, 1),
          reply_markup=create_pagination(callback.from_user.id)
     )

@router.callback_query(F.data == "<<", StateFilter(default_state))
async def process_prev(callback: CallbackQuery):
    if len_file(callback.from_user.id, user_db[callback.from_user.id]-1):
          user_db[callback.from_user.id] -= 1
          await callback.message.edit_text(
               text=lexicon["open"]+open_file(callback.from_user.id, user_db[callback.from_user.id]),
               reply_markup=create_pagination(callback.from_user.id)
          )
    else:
          await callback.answer(
              text=lexicon["open_error"],
              show_alert=True
         )

@router.callback_query(F.data == ">>", StateFilter(default_state))
async def process_next(callback: CallbackQuery):
    if len_file(callback.from_user.id, user_db[callback.from_user.id]):
          user_db[callback.from_user.id] += 1
          await callback.message.edit_text(
            text=lexicon["open"]+open_file(callback.from_user.id, user_db[callback.from_user.id]),
            reply_markup=create_pagination(callback.from_user.id)
          )
    else:
         await callback.answer(
              text=lexicon["open_error"],
              show_alert=True
         )