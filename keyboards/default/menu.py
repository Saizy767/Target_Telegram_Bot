from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Добавить запись'),
        ],
        [
            KeyboardButton(text='Задачи'),
            KeyboardButton(text='Удалить задачу'),
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True
)
