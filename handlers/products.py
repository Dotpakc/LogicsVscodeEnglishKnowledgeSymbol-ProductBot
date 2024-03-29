from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import any_state
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


from keyboards.main_user import main_user_kb, back_user_kb, basket_kb, get_products_kb
from utils.files import get_products, get_all_categories, get_products_by_category
from utils.paginator import paginator


main_router = Router()

class ProductState(StatesGroup):
    category = State()


@main_router.callback_query(F.data=="list_products", any_state)
async def callback_basket(call: types.CallbackQuery, state: FSMContext):
    print("list_products")
    await state.set_state(ProductState.category)
    await state.update_data(category="all")
    
    products = get_products()
    all_categories = get_all_categories()
    all_categories.remove('all') # видалили поточну категорію
    
    paginator_products = paginator(list(products.items()))
    kb = get_products_kb(paginator_products, len(products), categories=all_categories)
    
    text = "Список товарів:\n"
    for i, product in enumerate(paginator_products, 1):
        text += f"{i}. {product[1]['name']} - {product[1]['price']} грн\n"
        
    await call.message.edit_text(
        text=text,
        reply_markup=kb.as_markup()
    )
    
    
@main_router.callback_query(F.data.startswith("product_page_"), ProductState.category)
async def callback_product_page(call: types.CallbackQuery, state: FSMContext):
    page = int(call.data.split("_")[-1])
   
    data = await state.get_data()
    category = data.get("category")
    print("category", category)
   
    all_categories = get_all_categories()# ми отримали всі категорії Set
    all_categories.remove(category) # видалили поточну категорію
    
    if category=="all":
        products = get_products()
    else:
        products = get_products_by_category(category)
        
    paginator_products = paginator(list(products.items()), page=page)
    kb = get_products_kb(paginator_products, len(products), page=page, categories=all_categories)# передали всі категорії без поточної для відображення кнопок
    
    text = "Список товарів:\n"
    for i, product in enumerate(paginator_products, page * 5 + 1):
        text += f"{i}. {product[1]['name']} - {product[1]['price']} грн\n"
        
        
    await call.message.edit_text(
        text=text,
        reply_markup=kb.as_markup()
    )
    

@main_router.callback_query(F.data.startswith("category_"), ProductState.category)
async def callback_category(call: types.CallbackQuery, state: FSMContext):
    category = call.data.split("_")[-1]
    print("category", category)
    
    await state.update_data(category=category)
    
    
    
    
    all_categories = get_all_categories()# ми отримали всі категорії Set
    all_categories.remove(category) # видалили поточну категорію
    
    if category=="all":
        products = get_products()
    else:
        products = get_products_by_category(category)
        

    paginator_products = paginator(list(products.items()))
    
    kb = get_products_kb(paginator_products, len(products), categories=all_categories)# передали всі категорії без поточної для відображення кнопок
    
    text = f"Список товарів категорії {category}:\n"
    for i, product in enumerate(paginator_products, 1):
        text += f"{i}. {product[1]['name']} - {product[1]['price']} грн\n"
    
    await call.message.edit_text(
        text=text,
        reply_markup=kb.as_markup()
    )