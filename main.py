from aiogram import executor


from loader import dp
from sql.sql import add_data
from utils.notify_admins import on_startup_notify
from utils.set_bot_command import set_default_commands


async def on_startup(dp):
    # Downloading defaults commands
    await set_default_commands(dp),

    # Notifying about to start
    await on_startup_notify(dp)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
    add_data()
