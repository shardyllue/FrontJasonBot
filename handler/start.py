from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from core.db import AsyncSession

from sqlalchemy import select

import template.start as tstart
import module.base as mbase
import module.state as mstate

dp = Router()



@dp.message(Command(commands=["start"]))
async def start_handler(
    ctx : Message, 
    db : AsyncSession,
    state : FSMContext
) -> None:
    """
    
    Command /start call this handler
    
    """

    userbot = await db.execute(
        select(mbase.TokenTable).where(
            mbase.TokenTable.user_id == ctx.from_user.id
        )
    )

    if userbot.fetchone() is None:

        await ctx.answer(
            text=tstart.text.format(ctx=ctx),
            reply_markup=tstart.kb_start    
        )

        await state.set_state(
            mstate.RegisterState.is_can_register
        )

    else:
        await ctx.answer(
            text=tstart.text.format(ctx=ctx),
            reply_markup=tstart.kb_main    
        )

        await state.clear()
    

    return await db.close()



