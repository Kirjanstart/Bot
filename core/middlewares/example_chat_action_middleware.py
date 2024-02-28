from typing import  Any, Callable, Dict, Awaitable

from aiogram import BaseMiddleware
from aiogram.dispatcher.flags import get_flag
from aiogram.types import Message
from aiogram.utils.chat_action import ChatActionSender
from aiogram import Bot



class ExampleChatActionMiddleware(BaseMiddleware):

    def __init__(self, bot: Bot):
        super().__init__()
        self.bot = bot

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any],
    ) -> Any:
        chat_action = get_flag(data, 'chat_action')
        if not chat_action:
            return await handler(event, data)

        async  with ChatActionSender(bot=self.bot, action=chat_action, chat_id=event.chat.id):
            return await handler(event, data)
