from aiogram.types import Message
from aiogram.filters import BaseFilter

from config_reader import config
from other_fuctions.other_fuctions import open_file

class domain_expansion(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        d = open_file(message.from_user.id)
        return d == "Здесь пока пусто напиши что нибудь!"
