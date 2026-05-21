import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://ton-miner-farm.onrender.com")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton(
        text="🚀 Открыть ферму", 
        web_app=WebAppInfo(url=WEBAPP_URL)
    ))
    await message.answer("Добро пожаловать в TON Miner Farm!", reply_markup=keyboard)

if __name__ == "__main__":
    executor.start_polling(dp)
