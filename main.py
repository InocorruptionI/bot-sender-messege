import asyncio
import logging
import handlers

from aiogram import Dispatcher, Bot
from constants import TOKEN



bot = Bot(token=TOKEN)

dp = Dispatcher()


async def main():
    dp.include_router(handlers.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
