from aiogram.filters.base import Filter
from aiogram.types import Message, KeyboardButton



class Button(Filter):


    def __init__(self, btn: KeyboardButton) -> None:
        self.btn = btn

    async def __call__(self, ctx: Message) -> bool:
        return ctx.text == self.btn.text