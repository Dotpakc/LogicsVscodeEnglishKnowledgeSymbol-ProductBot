from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import any_state
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.enums import ParseMode

from aiogram.utils.formatting import Text, Bold, Italic, Code

from keyboards.main_user import main_user_kb, back_user_kb, basket_kb, get_product_kb
from utils.files import get_products, get_all_categories, get_products_by_category, find_product, get_user_cart
from utils.paginator import paginator


main_router = Router()

class ProductState(StatesGroup):
    view = State()


@main_router.callback_query(F.data.startswith("product_view_"), any_state)
async def callback_product_view(call: types.CallbackQuery, state: FSMContext):
    
    product_id = call.data.split("_")[-1]
    product = find_product(product_id)
    print(product)
    cart = get_user_cart(call.from_user.id)
    cart_ids = [product.get("id") for product in cart]
    
    kb = get_product_kb(cart_ids, product_id)
    
    text_1 = Text("📦 ", Bold(product.get("name")), "\n")
    text_1 += Text("📝 ", Italic(product.get("description")), "\n")
    text_1 += Text("💰 ", Bold("Ціна: "), Code(product.get("price")), "\n")
    text_1 += Text("🔗 ", Bold("Посилання: "), Code(product.get("url")), "\n")
    
    
    
    
    await call.message.answer_photo(
        photo=product.get("image"),
        caption=text_1.as_html(),
        reply_markup=kb.as_markup(),
        parse_mode=ParseMode.HTML
    )

