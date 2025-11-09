import os
from bot.config import settings

def upload_to_telegram_or_storage(path: str, quality: str):
    size = os.path.getsize(path)
    if size > settings.max_telegram_file_bytes:
        return f"https://external.example/{os.path.basename(path)}"
    else:
        return f"https://telegram.local/{os.path.basename(path)}"
