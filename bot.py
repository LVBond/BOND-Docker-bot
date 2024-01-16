# 1.Импорт библиотек
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message             # ловим все обновления этого типа 
from aiogram.filters.command import Command   # обрабатываем команды /start, /help и другие

from transliterate import translit


# 2. Инициализация объектов
# TOKEN = os.getenv('TOKEN')
bot = Bot(token="Твой токен от папы")                        # Создаем объект бота
dp = Dispatcher()                             # Создаем объект диспетчера. Все хэндлеры(обработчики) должны быть подключены к диспетчеру
logging.basicConfig(level=logging.INFO)

# Домашнее Задание
# - Включить запись log в файл
# - Бот принимает кириллицу отдаёт латиницу в соответствии с Приказом МИД по транслитерации
# - Бот работает из-под docker контейнера

def translit_text(text):
    translit_text = translit(text, 'ru', reversed=True)
    return translit_text


# 3. Обработка/Хэндлер на команду /start
@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}! Добро пожаловать в сервис транслитерации кириллицы в латиницу в соответствии с Приказом МИД России от 12.02.2020 № 2113. Отправьте текст на кириллице для получения результата.'
    logging.info(f'{user_name} {user_id} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)
    
# 4. Обработка/Хэндлер на любые сообщения
@dp.message()
async def send_echo(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text 
    logging.info(f'{user_name} {user_id}: {text}')
    await message.answer(text=translit_text(text))

# 5. Запуск процесса пуллинга
if __name__ == '__main__':
    dp.run_polling(bot)