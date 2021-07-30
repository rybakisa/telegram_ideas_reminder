import sched, time

import settings
from random_message_sender import RandomMessageSender


scheduler = sched.scheduler(time.time, time.sleep)
sender = RandomMessageSender(
    api_id=settings.TELEGRAM_API_ID,
    api_hash=settings.TELEGRAM_API_HASH,
    from_chat_id=settings.TELEGRAM_FROM_CHAT_ID,
    to_chat_id=settings.TELEGRAM_TO_CHAT_ID,
)

def run_job():
    sender.run()
    scheduler.enter(settings.SCHEDULER_DELAY_SECONDS, 1, run_job)
    
scheduler.enter(1, 1, run_job)
scheduler.run()
