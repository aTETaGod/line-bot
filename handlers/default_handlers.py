from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.types import Message
from aiogram.fsm.state import default_state

from dict.lexicon_ru import lexicon

router = Router()


@router.message(StateFilter(default_state))
async def process_all(message: Message):
    await message.answer(text=lexicon["other"])
