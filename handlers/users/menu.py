from loader import dp
from aiogram.types import Message
from keyboards.default.menu import main_menu
from aiogram.dispatcher.filters import Command


@dp.message_handler(Command('start'))
async def start(message: Message):
    await message.answer(text='Начинаем работу', reply_markup=main_menu),


@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
    await message.answer(text="Меню", reply_markup=main_menu),
