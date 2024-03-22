from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import any_state

from keyboards.main_user import main_user_kb, back_user_kb


main_router = Router()




@main_router.message(CommandStart(), any_state)
async def start(message: types.Message):
    await message.answer("Вітаю! Я бот для замовлення їжі. Обирайте що вам потрібно", reply_markup=main_user_kb.as_markup())

@main_router.callback_query(F.data=="back_user", any_state)
async def back_user(call: types.CallbackQuery):
    await call.message.answer("Головне меню", reply_markup=main_user_kb.as_markup())
    await call.message.delete()

@main_router.callback_query(F.data=="about_shop", any_state)
async def callback_about_shop(call: types.CallbackQuery):
    text=f'''Магазин "Їжа на дом" - це магазин з доставкою їжі.
    Ми працюємо з 10:00 до 22:00 щодня.
    Доставка від 30 хвилин.
    '''
    await call.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTqiQJGLeieXxyv5POCcYq1womncW5w_cna54SIx8Rxm39CNrprh69_XoEF2R3S-9ii3WE&usqp=CAU",
        caption=text,
        reply_markup=back_user_kb.as_markup()
    )
    await call.message.delete()
    
    
@main_router.callback_query(F.data=="support", any_state)
async def callback_support(call: types.CallbackQuery):
    text=f'''Підтримка клієнтів працює з 10:00 до 22:00 щодня.
    Телефон: +380123456789
    Email:asdasdSd@asdas.comp
    '''
    await call.message.edit_text(
        text=text,
        reply_markup=back_user_kb.as_markup()
    )
    
@main_router.callback_query(F.data=="delivery_payment", any_state)
async def callback_delivery_payment(call: types.CallbackQuery):
    text=f'''Доставка від 30 хвилин.
    Оплата готівкою або карткою.
    При замовленні від 500 грн доставка безкоштовна.
    
    '''
    await call.message.edit_text(
        text=text,
        reply_markup=back_user_kb.as_markup()
    )

@main_router.callback_query(F.data=="loyalty_program", any_state)
async def callback_loyalty_program(call: types.CallbackQuery):
    text=f'''Програма лояльності діє для всіх клієнтів.
    При кожному замовленні ви отримуєте 5% від суми замовлення на свій рахунок.
    '''
    await call.message.edit_text(
        text=text,
        reply_markup=back_user_kb.as_markup()
    )
