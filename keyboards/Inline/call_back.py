from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from handlers.states.add_message import AddMessage
from keyboards.default import main_menu
from loader import dp
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(state='*', text='cancel')
async def call_back(call: CallbackQuery, state: FSMContext):
    await call.message.answer(text='Вы вернулись в Меню', reply_markup=main_menu)
    await state.finish()


@dp.callback_query_handler(state='*', text='first_question')
async def rename_target(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer(text='Измените поставленную задачу', reply_markup=ReplyKeyboardRemove())
    await AddMessage.Back_message.set()
