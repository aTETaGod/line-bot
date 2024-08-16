from aiogram.fsm.state import StatesGroup, State, default_state
from aiogram.fsm.storage.memory import MemoryStorage

storage = MemoryStorage()


class FSM(StatesGroup):
    fill_append = State()
    fill_delete = State()
