import os
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User

from config_reader import config

class StartMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        user: User = data.get("event_from_user")
        path = f"{config.path}{user.id}.txt"
        if os.path.isfile(path):
            pass
        else:
            f = open(path, "w")
            f.close()
        result = await handler(event, data)

        return result
