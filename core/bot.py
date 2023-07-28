
from aiogram import Bot

from utils import config


class CliBot:
    """
    
    Create a object of the bot

    """

    def __init__(self) -> None:
        self.bot = Bot(
            token=config.TOKEN,
            parse_mode="HTML"
        )

    async def __aenter__(self):
        return self.bot
 

    async def __aexit__(self, *args):
        await self.bot.session.close()





