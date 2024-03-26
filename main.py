import asyncio
import datetime
import logging
import asyncpg
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from core.handlers.basic import get_start, get_photo, get_hello, get_location, get_inline
from core.handlers.contact import get_fake_contact, get_true_contact
from core.settings import settings
from core.filters.iscontact import IsTrueContact
from core.utils.commands import set_commands
from core.handlers.callback import select_macbook
from core.utils.callbackdata import MacInfo
from core.handlers.pay import order, pre_checkout_query, successful_payment, shipping_check
from core.middlewares.countermiddleware import CounterMiddleware
from core.middlewares.officehours import OfficeHoursMiddleware
from core.middlewares.apschedulermiddleware import SchedulerMiddleware
from core.middlewares.dbmiddleware import DbSession
from core.handlers import form
from core.utils.statesform import StepsForm
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from core.handlers import apsched
from datetime import datetime, timedelta
from core.handlers import send_media
from core.middlewares.example_chat_action_middleware import ExampleChatActionMiddleware


logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
dp = Dispatcher()


@dp.startup()
async def start_bot():
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен!')


@dp.shutdown()
async def stop_bot():
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен!')


async  def crete_pool():
    return await asyncpg.create_pool(user='postgres', password='3846', database='users',
                                            host= '127.0.0.1', port=5432, command_timeout=60)


async def begin():
    # dp.startup.register(start_bot)
    # dp.shutdown.register(stop_bot)
    # pool_connect = await crete_pool()
    # pool_connect = await asyncpg.create_pool(user='postgres', password='3846', database='users',
    #                                         host= '127.0.0.1', port=5432, command_timeout=60)


    # scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    # scheduler.add_job(apsched.send_message_time, trigger='date', run_date=datetime.now() + timedelta(seconds=10),
    #                   kwargs={'bot': bot})
    # scheduler.add_job(apsched.send_message_cron, trigger='cron', hour=datetime.now().hour,
    #                   minute=datetime.now().minute + 1, start_date=datetime.now(), kwargs={'bot': bot})
    # scheduler.add_job(apsched.send_message_interval, trigger='interval', seconds=60, kwargs={'bot': bot})
    # scheduler.start()


    # dp.update.middleware.register(DbSession(pool_connect))
    # dp.message.middleware.register(CounterMiddleware())
    # dp.message.middleware.register(OfficeHoursMiddleware())
    # dp.update.middleware.register(OfficeHoursMiddleware())
    # dp.update.middleware.register(SchedulerMiddleware(scheduler))
    dp.message.middleware.register(ExampleChatActionMiddleware(bot))


    dp.message.register(send_media.get_audio, Command(commands='audio'), flags={'chat_action': 'upload_document'})
    dp.message.register(send_media.get_document, Command(commands='document'), flags={'chat_action': 'upload_document'})
    dp.message.register(send_media.get_media_group, Command(commands='mediagroup'), flags={'chat_action': 'upload_photo'})
    dp.message.register(send_media.get_photo, Command(commands='photo'), flags={'chat_action': 'upload_photo'})
    dp.message.register(send_media.get_sticker, Command(commands='sticker'), flags={'chat_action': 'choose_sticker'})
    dp.message.register(send_media.get_video, Command(commands='video'), flags={'chat_action': 'upload_video'})
    dp.message.register(send_media.get_video_note, Command(commands='video_note'), flags={'chat_action': 'upload_video_note'})
    dp.message.register(send_media.get_voice, Command(commands='voice'), flags={'chat_action': 'upload_voice'})


    dp.message.register(form.get_form, Command(commands='form'))
    dp.message.register(form.get_name, StepsForm.GET_NAME)
    dp.message.register(form.get_last_name, StepsForm.GET_LAST_NAME)
    dp.message.register(form.get_age, StepsForm.GET_AGE)


    dp.message.register(order, Command(commands='pay'))
    dp.pre_checkout_query.register(pre_checkout_query)
    dp.message.register(successful_payment, F.successful_payment)
    dp.shipping_query.register(shipping_check)
    dp.message.register(get_inline, Command(commands='inline'))
    dp.callback_query.register(select_macbook, MacInfo.filter(F.model == 'pro'))
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
    asyncio.run(begin())
