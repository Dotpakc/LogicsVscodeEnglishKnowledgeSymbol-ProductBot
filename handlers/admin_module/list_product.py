import uuid

from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.utils import keyboard
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


from .admin import AdminStates, admin_main_kb, back_admin_kb
from utils.files import add_product, get_products

# from loader import bot

list_product_router = Router()



@list_product_router.callback_query(F.data=="list_products", AdminStates.admin)
async def help(call: types.CallbackQuery, state: FSMContext):
    
    text = "List of products\n"
    products = get_products()
    for i, product in enumerate(products.values(), 1):
        text += f"{i}. {product['name']} - {product['price']}- {product['quantity']} - {product['description']} - {product['category']}\n"

    
    
    await call.message.edit_text(text, reply_markup=back_admin_kb.as_markup())
    



        
