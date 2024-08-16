import time
from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import default_state

from filters.infinite_void import domain_expansion
from keyboards import kb_start
from keyboards.kb_cancel import keyboard_cancel_delete
from dict.lexicon_ru import lexicon
from fsm.fsm import FSM
from other_fuctions.other_fuctions import delete_lines, open_file


router = Router()

@router.message(domain_expansion(), StateFilter(FSM.fill_delete))
async def process_void(message: Message, state: FSMContext):
    await message.answer(text=lexicon["domain"])
    await message.answer(
        text=lexicon["cancel"],
        reply_markup=kb_start.keyboard
    )
    await state.clear()

@router.callback_query(domain_expansion(), StateFilter(default_state), F.data == "delete")
async def process_void_callback(callback: CallbackQuery, state: FSMContext):
    await callback.answer(text=lexicon["domain"])
    await callback.message.edit_text(
        text=lexicon["cancel"],
        reply_markup=kb_start.keyboard
    )
    await state.clear()

@router.message(Command(commands="cancel"), StateFilter(FSM.fill_delete))
async def process_cancel_command_fsm(message: Message, state: FSMContext):
    await message.answer(
        text=lexicon["cancel"],
        reply_markup=kb_start.keyboard
    )
    await state.clear()

@router.message(F.text, StateFilter(FSM.fill_delete))
async def process_delete_fsm(message: Message):
    a = delete_lines(message.from_user.id, message.text)
    if a == 1:
        await message.answer(
            text=lexicon['delete_start_1']+open_file(message.from_user.id),
            reply_markup=keyboard_cancel_delete
        )
    elif a == 2:
        await message.answer(
            text=lexicon["delete_value_error"]
        )
        time.sleep(2)
        await message.answer(
            text=lexicon['delete_start_1']+open_file(message.from_user.id),
            reply_markup=keyboard_cancel_delete
        )
    elif a == 3:
        await message.answer(
            text=lexicon["delete_index_error"]
        )
        time.sleep(2)
        await message.answer(
            text=lexicon["delete_start_1"]+open_file(message.from_user.id),
            reply_markup=keyboard_cancel_delete
        )
    elif a == 0:
        await message.answer(
            text=lexicon["delete_negative_error"]
        )
        time.sleep(2)
        await message.answer(
            text=lexicon["delete_start_1"]+open_file(message.from_user.id),
            reply_markup=keyboard_cancel_delete
        )

@router.callback_query(F.data == "delete" , StateFilter(default_state))
async def process_delete_lines(callback: CallbackQuery, state: FSMContext):
    await state.set_state(FSM.fill_delete)
    await callback.message.edit_text(
        text=lexicon["delete_start_1"]+open_file(callback.from_user.id)
    )
    time.sleep(1)
    await callback.message.answer(
        text=lexicon["delete_start_2"],
        reply_markup=keyboard_cancel_delete
    )

@router.callback_query(F.data == "cancel_delete", StateFilter(FSM.fill_delete))
async def process_cancel_fsm_callback(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer(
        text=lexicon["cancel"],
        reply_markup=kb_start.keyboard
    )
    await state.clear()
