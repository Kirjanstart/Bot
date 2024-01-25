# @dp.message(Command('start'))
# async def send_welcome(message: types.Message):
#     await message.answer(f'Привет!\nЯ Botty!\nОтправь мне любое своё имя!')
#
# @dp.message()
# async def echo(message: types.Message):
#     await message.reply(f'Привет {message.text}, ты супер!')
#
#
# @dp.message(Command('stop'))
# async def button_view(message: types.Message):
#     kb = [[types.KeyboardButton(text='Кнопка 1'), types.KeyboardButton(text='Кнопка 2')], ]
#     keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
#     await message.reply(f'Вот тебе две кнопки, развлекайся!', reply_markup=keyboard)
#
#
# @dp.message(Command('dice'))
# async def cmd_dice(message: types.Message, bot: Bot):
#     await bot.send_dice(-1002041267112, emoji=DiceEmoji.DICE)
