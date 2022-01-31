from aiogram import Dispatcher, types
from create_bot import dp, bot
import json, string

#@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, 'Приятного отдыха')

#@dp.message_handler(commands=['График'])
async def command_grafik(message : types.Message):
    await bot.send_message(message.from_user.id, 'Понедельник - Пятница: 10:00 - 18:00')

#@dp.message_handler(commands=['Контакты'])
async def command_contact(message : types.Message):
    await bot.send_message(message.from_user.id, '(+38) 063-769-69-00, (+38) 066-26-70-007, \ns.elephant.dnepr@gmail.com')

#@dp.message_handler(commands=['Адресс'])
async def command_location(message : types.Message):
    await bot.send_message(message.from_user.id, '49101, місто Дніпро, проспект Пушкіна, будинок 11')

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_grafik, commands=['График'])
    dp.register_message_handler(command_contact, commands=['Контакты'])
    dp.register_message_handler(command_location, commands=['Расположение'])    