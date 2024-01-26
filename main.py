import asyncio
import logging
from core.handlers.basic import get_start, get_photo
from aiogram import Bot, Dispatcher, F
from core.settings import settings

logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
dp = Dispatcher()


@dp.startup()
async def start_bot():
    await bot.send_message(settings.bots.admin_id, text='Бот запущен!')

@dp.shutdown()
async def stop_bot():
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен!')


async def main():
    # dp.startup.register(start_bot)
    # dp.shutdown.register(stop_bot)
    dp.message.register(get_start)
    dp.message.register(get_photo, F.photo)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
