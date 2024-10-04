from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio


api = ' '
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message):
    #print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_massages(message):
    #print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

#
# - печатает строку в консоли  . Запускается только когда написана команда '/start' в чате с ботом. (используйте соответствующий декоратор)
# (message)
# - печатает строку в консоли .
# Запускается при любом обращении не описанном ранее. (используйте соответствующий декоратор)



