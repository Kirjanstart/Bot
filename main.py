import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


logging.basicConfig(level=logging.INFO)
API_TOKEN = ''
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.reply(f'Привет!\nЯ Botty!\nОтправь мне любое сообщение и я на него отвечу!')

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)



async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
     asyncio.run(main())

@dp.message(Command('stop'))
async def stops(message):
    await dp.stop_polling()