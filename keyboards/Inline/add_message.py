from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

first_answer = InlineKeyboardMarkup()
first_answer.add(InlineKeyboardButton(text='НАЗАД', callback_data='cancel'))

second_answer = InlineKeyboardMarkup()
second_answer.add(InlineKeyboardButton(text='НАЗАД', callback_data='first_question'))
second_answer.add(InlineKeyboardButton(text='ГЛАВНОН МЕНЮ', callback_data='cancel'))
