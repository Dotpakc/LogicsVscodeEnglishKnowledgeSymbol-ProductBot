from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart

from loader import bot

main_router = Router()

@main_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Hello! I'm a bot!")
    await bot.send_message(message.chat.id, "Hello! I'm a bot!")

@main_router.message(Command("help"))
async def help(message: types.Message):
    await message.answer("Help message")


