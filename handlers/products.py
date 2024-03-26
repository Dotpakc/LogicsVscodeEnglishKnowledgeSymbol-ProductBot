from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import any_state

from keyboards.main_user import main_user_kb, back_user_kb, basket_kb, get_products_kb
from utils.files import get_or_create_user, get_user_cart, change_user, get_products
from utils.paginator import paginator

main_router = Router()




@main_router.callback_query(F.data=="list_products", any_state)
async def callback_basket(call: types.CallbackQuery):
    print("list_products")
    products = get_products()
    paginator_products = paginator(list(products.items()))
    kb = get_products_kb(paginator_products, len(products))
    text = "Список товарів:\n"
    for i, product in enumerate(paginator_products, 1):
        text += f"{i}. {product[1]['name']} - {product[1]['price']} грн\n"
    await call.message.edit_text(
        text=text,
        reply_markup=kb.as_markup()
    )
    
@main_router.callback_query(F.data.startswith("product_page_"), any_state)
async def callback_product_page(call: types.CallbackQuery):
    page = int(call.data.split("_")[-1])
    
    products = get_products()
    paginator_products = paginator(list(products.items()), page=page)
    kb = get_products_kb(paginator_products, len(products), page=page)
    text = "Список товарів:\n"
    for i, product in enumerate(paginator_products, 1):
        text += f"{i}. {product[1]['name']} - {product[1]['price']} грн\n"
    await call.message.edit_text(
        text=text,
        reply_markup=kb.as_markup()
    )