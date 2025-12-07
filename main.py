from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import asyncio

API_TOKEN = '8468846429:AAFlmiBdCQc3qZJhLlW9wk57uxZRnjWJms8'  # Replace with your bot token

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Handler for incoming messages
@dp.message_handler()
async def echo_message(message: Message):
    await message.reply(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
