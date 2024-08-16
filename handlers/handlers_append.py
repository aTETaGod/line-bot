from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import default_state

from keyboards import kb_start
from keyboards.kb_cancel import  keyboard_cancel_append
from dict.lexicon_ru import lexicon
from fsm.fsm import FSM
from other_fuctions.other_fuctions import append_lines


router = Router()

@router.message(Command(commands="cancel"), StateFilter(FSM.fill_append))
async def process_cancel_command_fsm(message: Message, state: FSMContext):
    await message.answer(
        text=lexicon["cancel"],
        reply_markup=kb_start.keyboard
    )
    await state.clear()

@router.message(F.text.len() <= 400, StateFilter(FSM.fill_append))
async def process_append_fsm(message: Message):
    a = append_lines(message.from_user.id, message.text)
    if not(a):
        print(message.from_user.id, message.from_user.username, message.text)

@router.message(F.text.len() > 400, StateFilter(FSM.fill_append))
async def process_dont_append_fsm(message: Message):
    await message.answer(
        text=lexicon["dont_append"]
    )

@router.callback_query(F.data == "append_text", StateFilter(default_state))
async def process_append_text(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text=lexicon["append_button"],
        reply_markup=keyboard_cancel_append
    )
    await state.set_state(FSM.fill_append)

@router.callback_query(F.data == "cancel_append", StateFilter(FSM.fill_append))
async def process_cancel_fsm_callback(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer(
        text=lexicon["cancel"],
        reply_markup=kb_start.keyboard
    )
    await state.clear()