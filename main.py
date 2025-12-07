import asyncio
from aiogram import Bot, Dispatcher, types

API_TOKEN = 'YOUR_BOT_TOKEN_HERE'  # Replace with your bot token

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Handler for messages
@dp.message()
async def echo_message(message: types.Message):
    await message.reply(message.text)

async def main():
    # Start polling
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
