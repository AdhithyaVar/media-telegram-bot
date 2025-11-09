from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def settings_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="File Settings", callback_data="setting:file")],
        [InlineKeyboardButton(text="OTT Accounts", callback_data="setting:ott")],
        [InlineKeyboardButton(text="Storage Providers", callback_data="setting:storage")],
        [InlineKeyboardButton(text="Audio/Subtitles", callback_data="setting:media")],
        [InlineKeyboardButton(text="Watermark & Metadata", callback_data="setting:wmmeta")],
    ])

def quality_post_keyboard(links: dict):
    row = []
    rows = []
    for quality, url in links.items():
        row.append(InlineKeyboardButton(text=quality, url=url))
        if len(row) == 2:
            rows.append(row)
            row = []
    if row:
        rows.append(row)
    return InlineKeyboardMarkup(inline_keyboard=rows)
