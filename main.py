import sched, time

import settings
from scheduler import Scheduler
from random_message_sender import RandomMessageSender


sender = RandomMessageSender(
    api_id=settings.TELEGRAM_API_ID,
    api_hash=settings.TELEGRAM_API_HASH,
    from_chat_id=settings.TELEGRAM_FROM_CHAT_ID,
    to_chat_id=settings.TELEGRAM_TO_CHAT_ID,
)
scheduler = Scheduler(sender.run, settings.SCHEDULER_DELAY_SECONDS)

scheduler.run()
