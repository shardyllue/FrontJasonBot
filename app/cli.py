from typing import List
from aiogram import Dispatcher, Router

from utils.logger import logger

from core import CliBot
from core.db import AsyncEngine
from core.middleware import Middeware

from core import create_sessionmaker





async def client(
    engine : AsyncEngine,
    routers : List[Router]
) -> None:
    """
    
    Start up client for telegram bot

    """
    

    dp = Dispatcher()

    dp.include_routers(*routers)
    dp.message.middleware(Middeware(
        create_sessionmaker(engine)
    ))

    try:
        async with CliBot() as bot:

            logger.info("Starting up")
            await dp.start_polling(bot)

    finally:
        logger.info("Stuting down")
