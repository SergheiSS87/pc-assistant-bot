
import openai
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import logging
import os

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        ["📂 Диагностика ПК", "🛡 Удаление вирусов"],
        ["⚙️ Оптимизация системы", "🧩 Подбор комплектующих"],
        ["❓ Задать вопрос"]
    ],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я GPT-бот, который поможет тебе с ремонтом и настройкой ПК.

"
        "Выбери опцию из меню или задай свой вопрос.",
        reply_markup=main_menu
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start — перезапуск бота
"
        "/help — справка
"
        "/about — информация о боте

"
        "Можешь также выбрать готовую тему из меню или задать свой вопрос вручную."
    )

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Я Telegram-бот, использующий ИИ ChatGPT, чтобы помогать с настройкой, диагностикой и обслуживанием компьютеров.
"
        "Создан ИТ-специалистом для таких же ИТ-специалистов и пользователей ПК."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text

    predefined_prompts = {
        "📂 Диагностика ПК": "Опиши пошаговую диагностику ПК при проблемах с включением или зависаниях.",
        "🛡 Удаление вирусов": "Как безопасно удалить вирусы с компьютера, не потеряв данные?",
        "⚙️ Оптимизация системы": "Дай советы по ускорению и оптимизации Windows без апгрейда железа.",
        "🧩 Подбор комплектующих": "Посоветуй комплектующие для бюджетного игрового ПК в пределах 1000$.",
        "❓ Задать вопрос": "Ты можешь задать мне свой вопрос о компьютерах, и я постараюсь помочь!"
    }

    prompt = predefined_prompts.get(user_input, user_input)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=800
        )
        reply = response['choices'][0]['message']['content']
    except Exception as e:
        logging.error(f"Ошибка OpenAI API: {e}")
        reply = "Произошла ошибка при обработке запроса. Попробуй позже."

    await update.message.reply_text(reply)

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
