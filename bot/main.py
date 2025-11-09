import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from bot.config import settings
from bot.routes import register_handlers
from bot.scheduler import start_scheduler

async def setup_bot():
    bot = Bot(token=settings.telegram_bot_token, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    register_handlers(dp)

    await bot.set_my_commands([
        BotCommand(command="start", description="Bot info"),
        BotCommand(command="add_series", description="Track a series (manual)"),
        BotCommand(command="settings", description="Manage settings"),
        BotCommand(command="status", description="Job/status overview"),
    ])

    if settings.enable_auto_scheduler:
        asyncio.create_task(start_scheduler(dp, bot))

    await dp.start_polling(bot)

def main():
    asyncio.run(setup_bot())

if __name__ == "__main__":
    main()
