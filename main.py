import asyncio
from aiogram import Bot, Dispatcher

from handlers import default_handlers, default_handlers_callback, handlers_delete, handlers_open, handlers_start, handlers_append
from middlewares.middlewares import StartMiddleware

from config_reader import config 

async def main():
    bot = Bot(token=config.bot_token) 
    dp = Dispatcher()

    dp.include_router(handlers_start.router)
    dp.include_router(handlers_open.router)
    dp.include_router(handlers_append.router)
    dp.include_router(handlers_delete.router)
    dp.include_routers(default_handlers.router, default_handlers_callback.router)
    handlers_start.router.message.middleware(StartMiddleware())

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
