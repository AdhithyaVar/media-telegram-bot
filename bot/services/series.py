import uuid
from aiogram.types import Message

SERIES = {}

async def add_series_prompt(message: Message):
    await message.answer("Send series details in format:\nSERIES_TITLE | SOURCE_URL | PROVIDER_KEY")

async def save_series(title: str, url: str, provider: str, requested_audio: list, requested_subs: list):
    series_id = str(uuid.uuid4())
    SERIES[series_id] = {
        "title": title,
        "url": url,
        "provider": provider,
        "requested_audio": requested_audio,
        "requested_subs": requested_subs,
        "tracked": True
    }
    return series_id

def list_series():
    return SERIES
