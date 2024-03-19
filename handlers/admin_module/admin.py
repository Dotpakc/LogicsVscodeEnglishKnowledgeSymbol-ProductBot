from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.utils import keyboard
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


from decouple import config

# from loader import bot

admin_router = Router()


class AdminStates(StatesGroup):
    admin = State()
    

admin_main_kb = keyboard.InlineKeyboardBuilder()
admin_main_kb.add(
    types.InlineKeyboardButton(text="🔵Cписок товарів", callback_data="list_products"),
    types.InlineKeyboardButton(text="🟢Додати товар", callback_data="add_product"),
    types.InlineKeyboardButton(text="🔴Видалити товар", callback_data="delete_product"),
    types.InlineKeyboardButton(text="🟠Редагувати товар", callback_data="edit_product")
    )
admin_main_kb.add(types.InlineKeyboardButton(text="🔵Список адміністратовів",callback_data="list_administrator"))

back_admin_kb = keyboard.InlineKeyboardBuilder()
back_admin_btn = types.InlineKeyboardButton(text="Назад", callback_data="back_admin")
back_admin_kb.add(back_admin_btn)


@admin_router.message(Command("admin"))
async def help(message: types.Message, command: CommandObject, state: FSMContext):
    if command.args != config('ADMIN_PASSWORD'):
        return
    await state.set_state(AdminStates.admin) # set state to admin
    await message.answer("You are admin", reply_markup=admin_main_kb.as_markup())
    
