# ==========================================(HEATER)====================================================================
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
# ============================================(MAIN)====================================================================
main_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text= 'О нас', callback_data= 'about'),
            InlineKeyboardButton(text= 'Каталог', callback_data= 'catalog'),

        ],[InlineKeyboardButton(text= 'Рассчитать калории', callback_data= 'calories')]
    ],resize_keyboard= True
)


main_manager = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text= 'Менеджер', callback_data= 'manager'),
            InlineKeyboardButton(text= 'Каталог', callback_data= 'catalog')
        ]
    ],resize_keyboard= True
)

kb_yandex = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text= 'Пояндексить', url= 'www.ya.ru'),
         InlineKeyboardButton(text= 'Назад', callback_data= 'back')]
    ],resize_keyboard= True
)

kb_var = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text= 'Изотоники', callback_data= 'izo')],
        [InlineKeyboardButton(text= 'Витамины', callback_data= 'vita')],
        [InlineKeyboardButton(text= 'Протеины', callback_data= 'protein')],
        [InlineKeyboardButton(text= 'Другие предолжения', callback_data= 'manager')],
        [InlineKeyboardButton(text= 'Назад', callback_data= 'back')]
        ]
)
kb_buy = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text= 'Купить', callback_data= 'buy')],
        [InlineKeyboardButton(text= 'Каталог', callback_data= 'catalog')]
        ]
)