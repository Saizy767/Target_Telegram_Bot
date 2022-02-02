from aiogram.dispatcher.filters.state import StatesGroup, State


class AddMessage(StatesGroup):
    Add_button = State()
    Add_message = State()
    Add_value_message = State()
    Back_message = State()
