from aiogram import Bot

async def send_message_cron(bot: Bot):
    await bot.send_message(5528605206, f'sent quote')