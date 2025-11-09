# Architecture Overview

## Flow
1. User triggers manual download (/download).
2. Job enqueued to Celery (download_job).
3. Provider plugin extracts stream metadata (no DRM bypass).
4. Validate requested audio/subtitle languages (strict all-or-none).
5. Download original master.
6. Apply watermark/image/text and metadata tags to original.
7. Transcode derivative qualities in parallel (future optimization: separate tasks).
8. Upload each variant:
   - If size <= limit: Telegram message (save message + link)
   - If size > limit: External storage plugin (S3, Mega, etc.)
9. Shorten each link via URL shortener plugin.
10. Post summary to channel with inline buttons (per quality).
11. Store job record with status.

## Plugins
- OTT Provider: providers/<provider>.py
- Storage: storage/<provider>.py
- Shortener: shorteners/<provider>.py
- Watermark: processors/watermark.py
- Metadata: processors/metadata.py

## Episode Auto Mode
- Scheduler polls each tracked series.
- Provider plugin fetches latest episode list.
- Compares with stored episodes.
- Queues new episodes' download jobs.

## Strict Multi-Audio Rule
If any requested language absent: abort job early with meaningful status.

## Security
- Encrypted credentials table (Fernet).
- Admin-only commands: manage providers, storage, global settings.

## Scaling
- Separate queues: discovery, download, transcode, upload.
- Horizontal workers; shared Redis + Postgres.

## Future Enhancements
- Progress reporting per job
- Retry policies
- Web dashboard
- Rate limiting per provider
