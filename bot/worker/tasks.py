import os
from bot.worker.celery_app import celery_app
from bot.config import settings
from bot.services.jobs import JOBS
from bot.utils.transcode import transcode_variants
from bot.utils.links import shorten_link
from bot.utils.upload import upload_to_telegram_or_storage

def extract_streams(provider_key: str, url: str):
    return {
        "available_audio": ["Japanese", "English"],
        "available_subs": ["English", "Japanese"],
        "download_url": url
    }

@celery_app.task(name="bot.worker.tasks.download_job")
def download_job(job_id: str):
    job = JOBS.get(job_id)
    if not job:
        return
    job["status"] = "downloading"

    series_id = job["series_id"]
    from bot.services.series import SERIES
    series = SERIES.get(series_id, {})
    stream_info = extract_streams(series.get("provider"), series.get("url"))

    requested_audio = series.get("requested_audio", [])
    for lang in requested_audio:
        if lang not in stream_info["available_audio"]:
            job["status"] = f"skip_missing_audio:{lang}"
            return

    requested_subs = series.get("requested_subs", [])
    for lang in requested_subs:
        if lang not in stream_info["available_subs"]:
            job["status"] = f"skip_missing_sub:{lang}"
            return

    original_path = f"{settings.storage_root}/{series_id}_original.mp4"
    open(original_path, "wb").write(b"FAKEVIDEO")
    job["status"] = "processing"

    variants = transcode_variants(original_path, settings.ffmpeg_path)

    quality_links = {}
    for quality, path in variants.items():
        link = upload_to_telegram_or_storage(path, quality)
        short = shorten_link(link)
        quality_links[quality] = short

    JOBS[job_id]["post"] = quality_links
    job["status"] = "completed"
    return quality_links

def enqueue_download_task(job_id: str):
    download_job.delay(job_id)

@celery_app.task(name="bot.worker.tasks.auto_discovery")
def auto_discovery(series_id: str):
    return {"series_id": series_id, "discovered": True}

def enqueue_auto_discovery_task(series_id: str):
    auto_discovery.delay(series_id)
