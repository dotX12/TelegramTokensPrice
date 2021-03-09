import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from handler import *

scheduler = AsyncIOScheduler()
scheduler.add_job(flood.delete_my_messages, "interval", seconds=10)
scheduler.start()
asyncio.get_event_loop().run_forever()
