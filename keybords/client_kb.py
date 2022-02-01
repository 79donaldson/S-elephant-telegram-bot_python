from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/График')
b2 = KeyboardButton('/Контакты')
b3 = KeyboardButton('/Расположение')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b1, b2).add(b3)