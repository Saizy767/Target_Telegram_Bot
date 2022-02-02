from aiogram.dispatcher.filters.state import StatesGroup, State


class DeleteMessage(StatesGroup):
    Delete_button = State()
    Delete_message = State()
