from aiogram.utils import keyboard


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
