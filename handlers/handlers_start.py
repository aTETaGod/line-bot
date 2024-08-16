from aiogram import Router
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import Message
from aiogram.fsm.state import default_state

from dict.lexicon_ru import lexicon
from keyboards import kb_start

router = Router()


@router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message):
    await message.answer(text=lexicon["/start"], reply_markup=kb_start.keyboard)

