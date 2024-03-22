from aiogram.fsm.state import State, StatesGroup


class AdminStates(StatesGroup):
    admin = State()

class AddProductStates(StatesGroup):
    name = State()
    price = State()
    quantity = State()
    description = State()
    image = State()
    category = State()
     