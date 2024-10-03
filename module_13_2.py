from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio


api = '8050141538:AAEQjto5Qn5-TnOnqeJZ7E-QB88d90o4WVo'
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler()
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

#
# - печатает строку в консоли  . Запускается только когда написана команда '/start' в чате с ботом. (используйте соответствующий декоратор)
# all_massages(message)
# - печатает строку в консоли 'Введите команду /start, чтобы начать общение.'.
# Запускается при любом обращении не описанном ранее. (используйте соответствующий декоратор)



