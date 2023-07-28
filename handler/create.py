from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from core.db import AsyncSession
from core.filters import Button

import template.start as tstart
import template.create as tcreate
import template.register as tregister

import module.state as mstate
import module.base as mbase

import utils.valid as uvalid


dp = Router()


@dp.message(
    Button(tstart.create),
    mstate.RegisterState.is_can_register,
)
async def create_bot_handler(
    ctx : Message, db : AsyncSession, state : FSMContext
):
    await ctx.answer(
        text=tcreate.text,
        reply_markup=tcreate.kb
    )
    
    await state.set_state(mstate.RegisterState.token)

    return await db.close()


@dp.message(mstate.RegisterState.token)
async def register_token_handler(
    ctx : Message, db : AsyncSession, state : FSMContext
):
    bot_token = ctx.text

    userbot = await uvalid.valid_token(bot_token)

    if not userbot:

        await ctx.answer(tregister.err_token)

        return await db.close()
        

    await ctx.answer(
        text=tregister.valid_token.format(userbot=userbot),
        reply_markup=tstart.kb_main
    )


    db.add(mbase.TokenTable(
        user_id = ctx.from_user.id,
        token=bot_token
    ))

    await state.clear()

    return await db.commit()

