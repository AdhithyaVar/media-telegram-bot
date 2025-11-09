from aiogram import Dispatcher, Router, F
from aiogram.types import Message, CallbackQuery
from bot.services.series import add_series_prompt, list_series
from bot.ui.keyboards import settings_keyboard
from bot.services.jobs import request_manual_download

router = Router()

def register_handlers(dp: Dispatcher):
    dp.include_router(router)

@router.message(F.text == "/start")
async def cmd_start(message: Message):
    await message.answer(
        "Welcome to the Media Automation Bot.\nUse /add_series to track a series or /settings to configure."
    )

@router.message(F.text == "/add_series")
async def cmd_add_series(message: Message):
    await add_series_prompt(message)

@router.message(F.text.startswith("/download"))
async def cmd_download(message: Message):
    parts = message.text.strip().split()
    if len(parts) < 3:
        await message.answer("Usage: /download <series_id> <ep_range e.g. 1-12>")
        return
    series_id = parts[1]
    ep_range = parts[2]
    job_id = await request_manual_download(series_id, ep_range, user_id=message.from_user.id)
    await message.answer(f"Queued download job: {job_id}")

@router.message(F.text == "/settings")
async def cmd_settings(message: Message):
    kb = settings_keyboard()
    await message.answer("Settings Menu:", reply_markup=kb)

@router.callback_query(F.data.startswith("setting:"))
async def cb_setting(callback: CallbackQuery):
    await callback.answer("Opening setting...")
