import asyncio
from loader import bot
from handlers import dp

async def main():
    print("Start bot")
    await dp.start_polling(bot)
    
    
if __name__ == "__main__":
    asyncio.run(main())
    