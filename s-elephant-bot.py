from aiogram import Bot, types
from aiogram.dispatcher import dispatcher
from aiogram.utils import executer

import os, json, string



bot = Bot(token=os.getenv('TOKEN'))  
dp = dispatcher(bot)

@dp.message_handler()
async def echo_send(message : types.Message):
    await message.aswer(message.text)
    await message.reply(message.text)
    await bot.send.message(message.from_user.id, message.text)




executor.start_polling(dp, skip_updates=True)