from celery import Celery
from bot.config import settings

celery_app = Celery(
    "media_bot",
    broker=settings.redis_url,
    backend=settings.redis_url,
)

celery_app.conf.task_routes = {
    "bot.worker.tasks.download_job": {"queue": "download"},
    "bot.worker.tasks.auto_discovery": {"queue": "discovery"},
}