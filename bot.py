
import os
import logging
import openai
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv

# Загрузка .env
load_dotenv()

# Настройки логирования
logging.basicConfig(level=logging.INFO)

# Токены
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# Инициализация бота и диспетчера
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

# Клавиатура
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("🛠 Советы по ПК")).add(KeyboardButton("ℹ️ О боте"))

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("Привет! Я NeoHelp — бот, который помогает с ремонтом и настройкой ПК. Выберите команду или напишите вопрос:", reply_markup=keyboard)

@dp.message_handler(commands=["help"])
async def help_handler(message: types.Message):
    await message.answer("Просто отправьте мне вопрос, связанный с компьютерами, и я постараюсь помочь.
Доступные команды:
/start — начать
/help — помощь
/about — о боте")

@dp.message_handler(commands=["about"])
async def about_handler(message: types.Message):
    await message.answer("🧠 Я использую ChatGPT для генерации ответов на вопросы по ремонту и настройке компьютеров.
Разработано NeoHelp.")

@dp.message_handler(lambda message: message.text == "🛠 Советы по ПК")
async def pc_tips(message: types.Message):
    await message.answer("Напишите конкретный вопрос, например: «Почему не включается компьютер?» или «Как установить Windows?»")

@dp.message_handler(lambda message: message.text == "ℹ️ О боте")
async def about_button(message: types.Message):
    await about_handler(message)

@dp.message_handler()
async def handle_message(message: types.Message):
    try:
        user_input = message.text.strip()
        if not user_input:
            await message.reply("Пожалуйста, введите текст запроса.")
            return

        logging.info(f"Запрос от пользователя @{message.from_user.username}: {user_input}")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )

        answer = response.choices[0].message.content
        await message.reply(answer)

    except Exception as e:
        logging.error(f"Ошибка при обработке запроса: {e}")
        await message.reply("Произошла ошибка при обработке запроса. Попробуйте позже.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
