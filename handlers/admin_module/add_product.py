import uuid

from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.utils import keyboard
from aiogram.fsm.context import FSMContext


from states.adminStates import AdminStates, AddProductStates
from .admin import admin_main_kb, back_admin_kb
from utils.files import add_product

# from loader import bot

add_product_router = Router()



# [
#     {
#         "name": "product_name",
#         "price": "product_price",
#         "quantity": "product_quantity",
#         "description": "product_description",
#         "image": "product_image file_id or url",
#         "category": "product_category"
#     }
# ]

@add_product_router.callback_query(F.data=="add_product", AdminStates.admin)
async def help(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("Enter product name", reply_markup=back_admin_kb.as_markup())
    await state.set_state(AddProductStates.name)

@add_product_router.message(AddProductStates.name)
async def name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Enter product price", reply_markup=back_admin_kb.as_markup())
    await state.set_state(AddProductStates.price)
    
@add_product_router.message(AddProductStates.price)
async def price(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Price must be a number", reply_markup=back_admin_kb.as_markup())
        return
    await state.update_data(price=message.text)
    await message.answer("Enter product quantity", reply_markup=back_admin_kb.as_markup())
    await state.set_state(AddProductStates.quantity)
    
@add_product_router.message(AddProductStates.quantity)
async def quantity(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Quantity must be a number", reply_markup=back_admin_kb.as_markup())
        return
    await state.update_data(quantity=message.text)
    await message.answer("Enter product description", reply_markup=back_admin_kb.as_markup())
    await state.set_state(AddProductStates.description)
    
@add_product_router.message(AddProductStates.description)
async def description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Enter product image or url of image", reply_markup=back_admin_kb.as_markup())
    await state.set_state(AddProductStates.image)
    
@add_product_router.message(AddProductStates.image, F.photo | F.text.startswith('http'))
async def image(message: types.Message, state: FSMContext):
    if message.photo:
        await state.update_data(image=message.photo[-1].file_id)
    else:
        await state.update_data(image=message.text)
    await message.answer("Enter product category", reply_markup=back_admin_kb.as_markup())
    await state.set_state(AddProductStates.category)
    
@add_product_router.message(AddProductStates.category)
async def category(message: types.Message, state: FSMContext):
    await state.update_data(category=message.text.lower())
    data = await state.get_data()
    data["id"] = uuid.uuid4().hex
    add_product(data)
    await state.clear()
    await state.set_state(AdminStates.admin)
    await message.answer("Product added", reply_markup=back_admin_kb.as_markup())
    


        
