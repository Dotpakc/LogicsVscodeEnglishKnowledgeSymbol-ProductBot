import logging

from aiogram import Bot, Dispatcher
from decouple import config


API_TOKEN = config('TELEGRAM_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()