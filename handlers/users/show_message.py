from aiogram.types import Message

from keyboards.default import main_menu
from loader import dp
from sql.sql import show_date


@dp.message_handler(text='Задачи')
async def button_show_message(message: Message):
    user_id = message.from_user.id
    if len(show_date(user_id)) != 0:
        await message.answer(text="Ваши задачи")
        target = []
        for num, text, value in show_date(user_id):
            value = 'Приоритет : ' + str(value)
            text = str(text)
            num = '№' + str(num)
            target.append(num)
            target.append(value)
            target.append(text)
            target.append('')
            # target = '№' + num + '\n' + 'Приоритет : ' + value + '\n' + text
        await message.answer('\n'.join(target))
        print("Show button")
    else:
        await message.answer(text="У вас нет задач", reply_markup=main_menu)
