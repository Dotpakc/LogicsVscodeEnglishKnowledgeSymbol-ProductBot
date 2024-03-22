import uuid

from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.utils import keyboard
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


from .admin import AdminStates, admin_main_kb, back_admin_kb, back_admin_btn
from utils.files import add_product, get_products , del_product

# from loader import bot

del_product_router = Router()



@del_product_router.callback_query(F.data=="delete_product", AdminStates.admin)
async def help(call: types.CallbackQuery, state: FSMContext):
    
    del_product_kb = keyboard.InlineKeyboardBuilder()
    
    text = "List of products\n"
    products = get_products()
    for i, product in enumerate(products.values(), 1):
        text += f"{i}. {product['name']} - {product['price']}- {product['quantity']} - {product['description']} - {product['category']}\n"
        del_product_kb.add(types.InlineKeyboardButton(text=f"🔴{i}", callback_data=f"del_product_{product['id']}"))

    del_product_kb.adjust(5)
    
    del_product_kb.row(back_admin_btn)
    
    await call.message.edit_text(text, reply_markup=del_product_kb.as_markup())
    

@del_product_router.callback_query(F.data.startswith("del_product_"), AdminStates.admin)
async def callback_query_del_product(call: types.CallbackQuery, state: FSMContext):
    
    
    print(call.data)
    product_id = call.data.split("_")[-1]
    del_product(product_id)
    await call.message.edit_text("Product deleted", reply_markup=back_admin_kb.as_markup())
    
    # await call.message.edit_text("Enter product name", reply_markup=back_admin_kb.as_markup())
    # await state.set_state(AddProductStates.name)