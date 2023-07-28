from typing import Callable, Dict, Awaitable, Any
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import Message

from utils.logger import logger
from core.db import async_sessionmaker



class Middeware(BaseMiddleware):
    """
    
    Custom Middleware for bot
    
    """

    def __init__(
        self, session : async_sessionmaker
    ) -> None:
        super().__init__()
        self.session = session
        

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        """
        
        Call
        
        """

        
        logger.info(f"{event.from_user.id}: {event.text}")
        data.setdefault("db", self.session())


        return await handler(event, data)