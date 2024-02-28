from aiogram.types import Message, FSInputFile, InputMediaPhoto, InputMediaVideo
from aiogram import Bot
from aiogram.utils.chat_action import ChatActionSender


async def get_audio(message: Message, bot: Bot):
    audio = FSInputFile(path=r'C:\Users\k.lavkin\Desktop\Trava_u_doma.mp3', filename='audio1.mp3')
    await  bot.send_audio(message.chat.id, audio=audio)


async def get_document(message: Message, bot: Bot):
    document = FSInputFile(path=r'C:\Users\k.lavkin\Desktop\Документ.docx')
    await bot.send_document(message.chat.id, document=document, caption='Это док')


async def get_media_group(message: Message, bot: Bot):
    photo1_mg = InputMediaPhoto(type='photo', media=FSInputFile(r'C:\Users\k.lavkin\Desktop\1.jpg'),
                               caption="It's media group")
    photo2_mg = InputMediaPhoto(type='photo', media=FSInputFile(r'C:\Users\k.lavkin\Desktop\2.webp'))
    video_mg = InputMediaVideo(type='video', media=FSInputFile(r'C:\Users\k.lavkin\Desktop\6.MP4'))
    media = [photo2_mg, photo1_mg, video_mg]
    await bot.send_media_group(message.chat.id, media)


async def get_photo(message: Message, bot: Bot):
    photo = FSInputFile(path=r'C:\Users\k.lavkin\Desktop\1.jpg')
    await  bot.send_photo(message.chat.id, photo=photo, caption='Это фото')


async def get_sticker(message: Message, bot: Bot):
    sticker = FSInputFile(path=r'C:\Users\k.lavkin\Desktop\2.webp')
    await  bot.send_sticker(message.chat.id, sticker=sticker)


async def get_video(message: Message, bot: Bot):
    # async with ChatActionSender.upload_video(chat_id=message.chat.id, bot=bot):
        video = FSInputFile(path=r'C:\Users\k.lavkin\Desktop\6.MP4')
        await  bot.send_video(message.chat.id, video=video, caption='Это видео')


async def get_video_note(message: Message, bot: Bot):
    # async with ChatActionSender.upload_video_note(chat_id=message.chat.id, bot=bot):
        video_note = FSInputFile(path=r'C:\Users\k.lavkin\Desktop\6.MP4')
        await  bot.send_video_note(message.chat.id, video_note=video_note)


async def get_voice(message: Message, bot: Bot):
    # async with ChatActionSender.record_voice(chat_id=message.chat.id, bot=bot):
        voice = FSInputFile(path=r'C:\Users\k.lavkin\Desktop\Trava_u_doma.opus')
        await  bot.send_voice(message.chat.id, voice=voice, caption='Это голосовуха')