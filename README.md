# OTT Media Telegram Automation Bot (Legal Use Only)

## Disclaimer
This project **must only be used for content you have legal rights to download, process, and redistribute**.
It does not include DRM circumvention logic. Violating OTT platform Terms of Service may be illegal.

## Features
- Manual & automatic episode acquisition
- Multi-quality encoding (Original + 1080p + 720p + 480p)
- Multi-audio and subtitle selection (strict all requested languages must exist)
- Metadata + watermark applied only to original master before derivative encodes
- Upload to Telegram (Video or Document) with fallback to external hosts for large files
- Link shortening + inline keyboard post generation
- Pluggable OTT provider modules & storage backends
- Job queue for scalable processing pipeline

## Quick Start (Development)
```bash
cp .env.example .env
docker compose up --build
```
Run migrations (later when Alembic added):
```bash
# placeholder
```
Start worker:
```bash
docker compose exec app celery -A bot.worker.celery_app worker -l INFO
```

## Architecture
See docs/architecture.md

## Security
- Secrets encrypted using Fernet (rotateable keys).
- Role-based command access.

## Legal
You are responsible for ensuring compliance with local laws and platform ToS.
