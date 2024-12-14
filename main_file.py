import logging
from aiogram import Dispatcher, Bot, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State

from keyboard import *

logging.basicConfig(level= logging.INFO)                           # <== проверка работы системы
dp = Dispatcher(Bot(token= 'API'),                   # << insert your TOKEN
                storage= MemoryStorage())

@dp.message_handler(commands= ['start'])
async def start(message):
    await message.answer(text= f'Добро пожаловать, {message.from_user.username}! ', reply_markup= main_kb)

@dp.callback_query_handler(text= 'about')
async def ab_out(call):
    with open('files/main_photo.jpg', 'rb') as img:
        await call.message.answer_photo(img, 'Мы занимаемся продажей спортивного питания уже много лет. '
                                              'По всем вопросам можете связаться с нашим менеджером.',
                                                reply_markup= main_manager)
        await call.answer()

@dp.callback_query_handler(text= 'catalog')
async def catalog_production(call):
    with open('files/catalog.jpg', 'rb') as catl:
        await call.message.answer_photo(catl, 'выберите напроваление которое вас интересует', reply_markup= kb_var)
    await call.answer()
# =======================================================================
class UserState(StatesGroup):
    age = State()
    growth = State() # рост
    weight = State() # вес
#
@dp.callback_query_handler(text='calories')
async def day_calories(call):
    await call.message.answer('Введите  свой возрас: ')
    await  UserState.age.set()
    await call.answer()
#
@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age= message.text)
    await message.answer('Введите свой рост: ')
    await UserState.growth.set()

@dp.message_handler(state= UserState.growth)
async def  set_weight(message, state):
    await state.update_data(growth= message.text)
    await message.answer('Введите свой вес: ')
    await UserState.weight.set()

@dp.message_handler(state= UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight= message.text)
    data = await state.get_data()
    # print(type(data['age']))
    result = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    await message.answer(f'Ваша норма калорий: {result}')
    await state.finish()
#============================================================================

@dp.callback_query_handler(text= 'manager')
async def manager_help(call):
    with open('files/main_manager.jpg', 'rb') as man:
        await call.message.answer_photo(man, 'По любым дополнтиельным вопросам вы можете '
                                             'написать мне @manager или поЯндексить))',
                                        reply_markup= kb_yandex)
    await call.answer()


@dp.callback_query_handler(text= 'back')
async def back_main(call):
    with open('files/main_photo.jpg', 'rb') as img:
        await  call.message.answer_photo(img, 'Выберите интерсующий раздел: ', reply_markup= main_kb)
    await call.answer()

@dp.callback_query_handler(text= 'izo')
async def izoton(call):
    with open('files/izotonic.jpg', 'rb') as img:
        await  call.message.answer_photo(img, 'Выберите интерсующий раздел: ', reply_markup= kb_buy)
    await call.answer()

@dp.callback_query_handler(text= 'vita')
async def izoton(call):
    with open('files/vitamin.jpg', 'rb') as img:
        await  call.message.answer_photo(img, 'Выберите интерсующий раздел: ', reply_markup= kb_buy)
    await call.answer()

@dp.callback_query_handler(text= 'protein')
async def izoton(call):
    with open('files/protein.jpg', 'rb') as img:
        await  call.message.answer_photo(img, 'Выберите интерсующий раздел: ', reply_markup= kb_buy)
    await call.answer()

@dp.callback_query_handler(text= 'buy')
async def call_buy(call):
    await call.message.answer('Вы приобрели данный товар')
    await call.answer()

if __name__ == '__main__':
    executor.start_polling(dp,)
