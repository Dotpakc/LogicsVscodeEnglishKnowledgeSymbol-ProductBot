from aiogram.utils import keyboard

from utils.paginator import paginator

main_user_kb = keyboard.InlineKeyboardBuilder()
# 📃 Товари
# 🛒 Кошик 📊 Замовлення
# 👉 Про Магазин 💬 Підтримка клієнтів
# 📦 Доставка та оплата 🎁 Програма лояльності
main_user_kb.row(
    keyboard.InlineKeyboardButton(text="📃 Товари", callback_data="list_products"),
)
main_user_kb.row(
    keyboard.InlineKeyboardButton(text="🛒 Кошик", callback_data="basket"),
    keyboard.InlineKeyboardButton(text="📊 Замовлення", callback_data="orders"),
)
main_user_kb.row(
    keyboard.InlineKeyboardButton(text="👉 Про Магазин", callback_data="about_shop"),
    keyboard.InlineKeyboardButton(text="💬 Підтримка клієнтів", callback_data="support"),
)
main_user_kb.row(
    keyboard.InlineKeyboardButton(text="📦 Доставка та оплата", callback_data="delivery_payment"),
    keyboard.InlineKeyboardButton(text="🎁 Програма лояльності", callback_data="loyalty_program"),
)   


# 👈 Повернутись назад
back_user_kb = keyboard.InlineKeyboardBuilder()
back_user_kb_btn = keyboard.InlineKeyboardButton(text="👈 Повернутись назад", callback_data="back_user")
back_user_kb.add(back_user_kb_btn)

 
#Додай Іконки
#Меню Карзини 
basket_kb = keyboard.InlineKeyboardBuilder()
# Купити
# Очистити кошик
# Назад

basket_kb.row(
    keyboard.InlineKeyboardButton(text="🛒 Купити", callback_data="buy_cart"),
    keyboard.InlineKeyboardButton(text="🗑️ Очистити кошик", callback_data="clear_cart"),
)
basket_kb.row(
    back_user_kb_btn
)


def get_product_kb(cart, product_id):
    # Додати в кошик
    # if product in cart -> Видалити з кошика
    # лінк на сайт
    # Назад
    
    product_kb = keyboard.InlineKeyboardBuilder()
    
    if product_id in cart:
        product_kb.add(
            keyboard.InlineKeyboardButton(text="🗑️ Видалити з кошика", callback_data=f"remove_from_cart_{product_id}")
        )
    else:
        product_kb.add(
            keyboard.InlineKeyboardButton(text="🛒 Додати в кошик", callback_data=f"add_to_cart_{product_id}")
        )
        
    # product_kb.add(
    #     keyboard.InlineKeyboardButton(text="🔗 Перейти на сайт", url=product['url'])
    # )
    
    product_kb.add(
        back_user_kb_btn
    )
    
    return product_kb





#Products kb list
def get_products_kb(products, products_len, page=0, per_page=5, categories=None):
    products_kb = keyboard.InlineKeyboardBuilder()
    
    if page > 0:
        products_kb.add(
            keyboard.InlineKeyboardButton(text="👈", callback_data=f"product_page_{page-1}")
        )
    print(page, products_len, per_page, products_len // per_page)
    if page < products_len // per_page:
        products_kb.add(
            keyboard.InlineKeyboardButton(text="👉", callback_data=f"product_page_{page+1}")
        )
        
   
    
    products_kb.row(
        *[
            keyboard.InlineKeyboardButton(text=f"{i}", callback_data=f"product_view_{product[0]}") 
            for i, product in enumerate(products, page * per_page + 1) 
        ]
    )
    
    if categories:
        products_kb.row(
            *[
                keyboard.InlineKeyboardButton(text=f"{category}", callback_data=f"category_{category}") 
                for category in categories
            ]
        )
    
    
    products_kb.row(
        keyboard.InlineKeyboardButton(text="👈 Назад", callback_data="back_user"),
    )
    
    return products_kb

