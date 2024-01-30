import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from core.handlers.basic import get_start, get_photo, get_hello, get_location
from core.handlers.contact import get_fake_contact, get_true_contact
from core.settings import settings
from core.filters.iscontact import IsTrueContact
from core.utils.commands import set_commands


logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
dp = Dispatcher()


@dp.startup()
async def start_bot():
    # await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен!')


@dp.shutdown()
async def stop_bot():
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен!')


async def main():
    # dp.startup.register(start_bot)
    # dp.shutdown.register(stop_bot)
    dp.message.register(get_start, Command('start'))
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_location, F.location)
    dp.message.register(get_hello, F.text == 'Привет')
    dp.message.register(get_true_contact, F.contact, IsTrueContact())
    dp.message.register(get_fake_contact, F.contact)


    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
