from aiogram.dispatcher.filters.state import StatesGroup, State

class PersonalData(StatesGroup):
    fullname = State()
    email = State()
    phoneNum = State()
