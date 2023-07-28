from aiogram.fsm.state import State, StatesGroup


class RegisterState(StatesGroup):

    is_can_register = State()
    token = State()