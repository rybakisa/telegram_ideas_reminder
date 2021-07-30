import settings
from scheduler import Scheduler
from random_message_sender import RandomMessageSender


sender = RandomMessageSender(
    api_id=settings.TELEGRAM_API_ID,
    api_hash=settings.TELEGRAM_API_HASH,
    send_from=settings.TELEGRAM_FROM_CHAT_LINK,
    send_to=settings.TELEGRAM_TO_CHAT_LINK,
)
scheduler = Scheduler(sender.run, settings.SCHEDULER_DELAY_SECONDS)

scheduler.run()
