from pydantic import BaseSettings
from typing import List, Optional

class Settings(BaseSettings):
    telegram_bot_token: 7518672889:AAFviSPzrazXxOShSdDTr4FzuSjrYn85paI
    telegram_api_id: Optional[int] = 28390734  # if using pyrogram
    telegram_api_hash: Optional[str] = d19bc2567b1f7e98fcc368cd185a74d9

    redis_url: str = "redis://redis:6379/0"
    database_url: str = "postgresql+psycopg://user:password@db:5432/ottbot"
    storage_root: str = "/data"
    max_telegram_file_bytes: int = 2_000_000_000  # 2GB default
    premium_limit_bytes: int = 4_000_000_000

    fernet_key: str  # generate with: python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
    url_shortener_provider: str = "bitly"
    bitly_token: Optional[str] = None

    enable_auto_scheduler: bool = True
    auto_poll_interval_minutes: int = 30

    allowed_video_container_extensions: List[str] = ["mp4", "mkv"]
    ffmpeg_path: str = "ffmpeg"
    yt_dlp_path: str = "yt-dlp"

    class Config:
        env_file = ".env"

settings = Settings()
