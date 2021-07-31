import random

from telethon.tl.types import MessageService
from telethon import TelegramClient


class RandomMessageSender:
    def __init__(self, api_id, api_hash, send_from, send_to):
        self.client = TelegramClient(
            'anon',
            api_id=api_id,
            api_hash=api_hash
        )
        self.send_from = send_from
        self.send_to = send_to

    async def __send_random_message(self):
        dialogs = await self.client.get_dialogs()
        send_from_entity = await self.client.get_entity(self.send_from)
        send_to_entity = await self.client.get_entity(self.send_to)

        messages = await self.client.get_messages(
            send_from_entity,
            limit=None,
        )
        messages = list(filter(lambda msg: not isinstance(msg, MessageService), messages))
        random_message = random.choice(messages)

        await self.client.forward_messages(
            entity=send_to_entity,
            messages=random_message,
            from_peer=send_from_entity,
        )

    def run(self):
        with self.client as client:
            client.loop.run_until_complete(
                self.__send_random_message()
            )
