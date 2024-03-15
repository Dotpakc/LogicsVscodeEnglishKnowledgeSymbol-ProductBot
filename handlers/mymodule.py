from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart

from loader import bot

main_router = Router()


@main_router.message(Command("lol"))
async def help(message: types.Message):
    await message.answer("LOL message")

