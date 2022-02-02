from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from handlers.states.delete_message import DeleteMessage
from keyboards.Inline.add_message import first_answer
from keyboards.default import main_menu
from keyboards.default.number_menu import number_menu
from loader import dp
from sql.sql import show_date, delete_date, show_date_enumerating


@dp.message_handler(text='Удалить задачу')
async def button_show_message(message: Message, state: FSMContext):
    user_id = message.from_user.id
    target = []
    if len(show_date(user_id=user_id)) != 0:
        await message.answer(text="Ваши задачи")
        for num, text, value in show_date(user_id):
            value = 'Приоритет : ' + str(value)
            text = str(text)
            num = '№' + str(num)
            target.append(num)
            target.append(value)
            target.append(text)
            target.append('')
        await message.answer('\n'.join(target))
        print("Show button")
        await (message.answer(text='Выберите выполненую задачу', reply_markup=number_menu))
        await (message.answer(text='Вернуться назад', reply_markup=first_answer))
        await DeleteMessage.Delete_message.set()
        await state.update_data(delete_button=message.text)
    else:
        await message.answer(text="У вас нет задач", reply_markup=main_menu)


@dp.message_handler(state=DeleteMessage.Delete_message)
async def check_number(message: Message, state: FSMContext):
    message_value = message.text
    user_id = message.from_user.id
    if (message.text != '/add') is True or \
            (message.text != '/menu') is True or \
            (message.text != '/help') is True:
        if message_value.isdigit() is True and \
                (0 < int(message_value) > 11) is False and \
                isinstance(int(message_value), int):
            array = []
            for (dic_num,) in show_date_enumerating(user_id=user_id):
                array.append(dic_num)
                pass
            if int(message_value) in array:
                await DeleteMessage.Delete_message.set()
                await state.update_data(delete_number=message.text)
                delete_date(deleted_text=message_value, user_id=user_id)
                await state.finish()
                print("set_message 3/3")
                await message.answer(text="Запись удалина", reply_markup=main_menu)
            else:
                await message.answer(text='Данной записи нет', reply_markup=main_menu)
                await state.finish()
        else:
            await message.answer(text='Введите число для удаления')
    else:
        await message.answer(text='Если хотите воспользоваться командой, нажмите на кнопку "Главное меню"')
