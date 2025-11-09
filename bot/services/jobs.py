import uuid
from bot.worker.tasks import enqueue_download_task

JOBS = {}

async def request_manual_download(series_id: str, ep_range: str, user_id: int):
    job_id = str(uuid.uuid4())
    JOBS[job_id] = {
        "series_id": series_id,
        "ep_range": ep_range,
        "user_id": user_id,
        "status": "queued"
    }
    enqueue_download_task(job_id)
    return job_id
