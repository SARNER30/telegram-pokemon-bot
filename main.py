# main.py
   from aiogram import Bot, Dispatcher, executor
   import os

   bot = Bot(token=os.getenv('API_TOKEN'))
   dp = Dispatcher(bot)

   @dp.message_handler(commands=['start'])
   async def start(message):
       await message.answer("Бот работает!")

   if __name__ == '__main__':
       executor.start_polling(dp)