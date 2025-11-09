import asyncio
from bot.services.series import list_series
from bot.worker.tasks import enqueue_auto_discovery_task

async def start_scheduler(dp, bot):
    from bot.config import settings
    interval = settings.auto_poll_interval_minutes * 60
    while True:
        for series_id, series in list_series().items():
            if series.get("tracked"):
                enqueue_auto_discovery_task(series_id)
        await asyncio.sleep(interval)
