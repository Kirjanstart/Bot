import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


logging.basicConfig(level=logging.INFO)
API_TOKEN = '6861695078:AAEsMfeI4mbt_HreAEUmsVcAYV83ZrGdttM'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.answer(f'Привет!\nЯ Botty!\nОтправь мне любое своё имя!')

@dp.message()
async def echo(message: types.Message):
    await message.reply(f'Привет {message.text}, ты супер!')



@dp.message(Command('stop'))
async def button_view(message: types.Message):
    kb = [[types.KeyboardButton(text='Кнопка 1'), types.KeyboardButton(text='Кнопка 2')], ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.reply(f'Вот тебе две кнопки, развлекайся!', reply_markup=keyboard)





async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
     asyncio.run(main())