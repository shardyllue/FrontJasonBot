from aiogram import Router
from aiogram.types import Message

from core.db import AsyncSession
from core.filters import Button

from sqlalchemy import select

import template.start as tstart
import template.price as tprice

dp = Router()


@dp.message(Button(tstart.price))
async def price_handler(
    ctx : Message,
    db : AsyncSession,
):
    
    await ctx.answer(
        text=tprice.text,
        reply_markup=tprice.kb
    )


    return await db.close()
