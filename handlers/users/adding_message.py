from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from handlers.states.add_message import AddMessage
from keyboards.Inline.add_message import first_answer, second_answer
from keyboards.default import main_menu
from keyboards.default.number_menu import number_menu
from loader import dp
from sql.sql import list_date, add_to_date, show_date, show_date_enumerating


@dp.message_handler(Command('add'))
async def command_add_message(message: Message, state: FSMContext):
    await message.answer(text="Введите текст", reply_markup=first_answer)
    await AddMessage.Add_button.set()
    await state.update_data(command_text=message.text)


@dp.message_handler(text='Добавить запись')
async def button_add_message(message: Message, state: FSMContext):
    await message.answer(text="Введите текст", reply_markup=first_answer)
    await AddMessage.Add_button.set()
    await state.update_data(button_text=message.text)


@dp.message_handler(state='*', commands='cancel')
async def cancel_handler(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await message.answer(text='Вы вернулись в Меню', reply_markup=main_menu)
    await state.finish()


@dp.message_handler(state=AddMessage.Add_button)
async def set_message(message: Message, state: FSMContext):
    user_id = message.from_user.id
    list_list = list_date(user_id=user_id) + 1
    if list_list < 11 and len(show_date(user_id)) < 11:
        if (message.text != '/add') is True or \
                (message.text != '/menu') is True or \
                (message.text != '/help') is True:
            await AddMessage.Add_message.set()
            await state.update_data(user_message=message.text)
            await message.answer(text="Если хотите вернуться \n"
                                      "Нажмите кнопку", reply_markup=second_answer)
            await message.answer(text='Выставите приоритет задачи', reply_markup=number_menu)
        else:
            await message.answer(text='Если хотите воспользоваться командой, нажмите на кнопку "Назад"')
    else:
        await message.answer(text='Вы превысили колличество добаления записей. Выполните одну из добавленных задач,'
                                  ' чтобы поставить перед собой следующие', reply_markup=main_menu)
        await state.finish()


@dp.message_handler(state=AddMessage.Back_message)
async def back_message(message: Message, state: FSMContext):
    user_id = message.from_user.id
    list_list = list_date(user_id=user_id) + 1
    if list_list < 11 and len(show_date(user_id)) < 11:
        if (message.text != '/add') is True or \
                (message.text != '/menu') is True or \
                (message.text != '/help') is True:

            await AddMessage.Add_message.set()
            await state.update_data(user_message=message.text)
            await message.answer(text="Если хотите вернуться \n"
                                      "Нажмите кнопку", reply_markup=second_answer)
            await message.answer(text='Выставите приоритет задачи', reply_markup=number_menu)
        else:
            await message.answer(text='Если хотите воспользоваться командой, нажмите на кнопку "Назад"')
    else:
        await message.answer(
            text='Вы превысили колличество добаления записей. Выполните одну из добавленных задач,'
                 ' чтобы поставить перед собой следующие', reply_markup=main_menu)
        await state.finish()


@dp.message_handler(state=AddMessage.Add_message)
async def set_message_value(message: Message, state: FSMContext):
    data = await state.get_data()
    message_value = message.text
    user_message = data.get("user_message")
    user_id = message.from_user.id

    if (message.text != '/add') is True or \
            (message.text != '/menu') is True or \
            (message.text != '/help') is True:
        if message_value.isdigit() is True and \
                (0 < int(message_value) > 11) is False and \
                isinstance(int(message_value), int):
            await AddMessage.Add_value_message.set()
            await state.update_data(message_value=message.text)
            array = []
            for (dic_num,) in show_date_enumerating(user_id=user_id):
                array.append(dic_num)

            z_counter = 1
            if array is False:
                counter = 1

            elif (10 not in array) is True and array is True:
                counter = array.sort()[-1] + 1

            else:
                z_counter = 1
                for num in array:
                    print(num, z_counter)
                    if z_counter != num:
                        counter = z_counter
                        break
                    z_counter += 1

            add_to_date(user_id=user_id,
                        user_message=data.get("user_message"),
                        message_value=message_value,
                        enumerate_text=z_counter)
            await state.finish()

            await message.answer(text="Запись добавлена", reply_markup=main_menu)
        else:
            await message.answer(text='Введите число приоритета')
    else:
        await message.answer(text='Если хотите воспользоваться командой, нажмите на кнопку "Главное меню"')
