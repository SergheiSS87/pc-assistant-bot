
# PC Assistant Bot

Это Telegram-бот, использующий ChatGPT для помощи в ремонте и настройке компьютеров. Работает на Python и развёртывается бесплатно на [Render.com](https://render.com/).

## 🚀 Возможности

- Поддержка команд `/start`, `/help`, `/about`
- Меню с кнопками для популярных ИТ-запросов
- Возможность задать произвольный вопрос
- Интеграция с OpenAI ChatGPT (gpt-3.5-turbo)

## 🧰 Установка локально

```bash
git clone https://github.com/yourusername/pc-assistant-bot.git
cd pc-assistant-bot
pip install -r requirements.txt
export TELEGRAM_TOKEN=ваш_телеграм_токен
export OPENAI_API_KEY=ваш_openai_ключ
python bot.py
```

## ☁️ Развёртывание на Render

1. Зарегистрируйтесь или войдите на [render.com](https://render.com/)
2. Создайте Web Service, подключив этот репозиторий
3. Укажите переменные окружения:
```
TELEGRAM_TOKEN=ваш_телеграм_токен
OPENAI_API_KEY=ваш_openai_ключ
```

## 📁 Структура

- `bot.py` — код бота
- `requirements.txt` — зависимости
- `Procfile` — запуск на Render
- `.gitignore` — игнорируемые файлы
- `logo.png` — логотип
