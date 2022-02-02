from aiogram import Dispatcher

from data import config


async def on_startup_notify(dp: Dispatcher):
    await dp.bot.send_message(config.admin_id, 'Let is go')
