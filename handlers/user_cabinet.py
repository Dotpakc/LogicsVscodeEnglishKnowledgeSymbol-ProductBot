from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import any_state

from keyboards.main_user import main_user_kb, back_user_kb, basket_kb
from utils.files import get_or_create_user, get_user_cart, change_user

main_router = Router()




@main_router.callback_query(F.data=="basket", any_state)
async def callback_basket(call: types.CallbackQuery):
    user, _ = get_or_create_user(call.from_user.id)
    cart = user.get("cart", {})
    text = "Ваш кошик пустий"
    if cart:
        text = "Ваш кошик:\n"
        for product in get_user_cart(call.from_user.id):
            text += f"{product['name']} - {product['price']} грн\n"
        
    await call.message.edit_text(
        text=text,
        reply_markup=basket_kb.as_markup()
    )
            
            
@main_router.callback_query(F.data=="clear_cart", any_state)
async def callback_clear_cart(call: types.CallbackQuery):
    user, _ = get_or_create_user(call.from_user.id)
    user["cart"] = []
    change_user(call.from_user.id, user)
    await call.message.edit_text(
        text="Кошик очищено",
        reply_markup=main_user_kb.as_markup()
    )
    
