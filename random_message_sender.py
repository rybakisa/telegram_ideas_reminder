import random
from telethon import TelegramClient


class RandomMessageSender:
    def __init__(self, api_id, api_hash, from_chat_id, to_chat_id):
        self.client = TelegramClient(
            'anon',
            api_id=api_id,
            api_hash=api_hash
        )
        self.from_chat_id = from_chat_id
        self.to_chat_id = to_chat_id

    async def __send_random_message(self, from_chat_id, to_chat_id):
        messages = await self.client.get_messages(from_chat_id, limit=None)
        random_message = random.choice(messages)
        await self.client.forward_messages(to_chat_id, random_message)

    def run(self):
        with self.client as client:
            client.loop.run_until_complete(
                self.__send_random_message(
                    self.from_chat_id,
                    self.to_chat_id,
                )
            )
