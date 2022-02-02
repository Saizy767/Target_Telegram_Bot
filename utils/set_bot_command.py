from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand('menu', "Показать меню"),
            types.BotCommand('add', "Добавить запись"),
            types.BotCommand('cancel', "Вернуться в меню"),
        ]
    )
