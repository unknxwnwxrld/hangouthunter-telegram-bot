# 🔍 HangoutHunter Telegram Bot

**Intelligent Telegram bot for discovering atmospheric venues**

The bot understands natural language queries (Russian, English, Ukrainian) and recommends 10–20 real restaurants, cafes, bars, and other spots — focusing on unique concepts, high ratings, and authentic experiences. No tourist traps or large chains.

Perfect when you just want to write: “cozy vegetarian cafe in central Moscow, affordable”.

### ✨ Features

- 🧠 Natural language processing via Google Gemini (through backend API)
- 🌍 Support for any city
- 🌐 Responses in the user’s chosen language
- 🎯 Priority to unique concepts, atmosphere, and quality
- 🚫 Strict prompt rules — only real, existing venues
- ⌨️ User-friendly interface with inline buttons and states

### 🤖 Live Bot

The bot is available on Telegram: [@HangoutHunterBot](https://t.me/HangoutHunterBot) (replace with your actual username after deployment).

### 🛠 Backend API

The bot communicates directly with the FastAPI backend:  
[hangouthunter-api](https://github.com/unknxwnwxrld/hangouthunter-api)

### 🚀 Quick Start

```
git clone https://github.com/unknxwnwxrld/hangouthunter-telegram-bot.git
cd hangouthunter-telegram-bot

cp .env.example .env  # add BOT_TOKEN and API_URL
pip install -r requirements.txt

python bot.py
```

The bot will start in polling mode. For production, webhook setup is recommended.

### 📸 Usage Examples

To get recommendations:

1. **Choose language** — select Russian, English, or Ukrainian when starting the bot.
2. **Specify city** — either:
   - Tap the button to **automatically share your location** (the bot will determine the city), or
   - Manually type the city name.
3. **Enter your criteria** — describe what you’re looking for in free form.

Examples of criteria:
- “Cozy bar with live music in Saint Petersburg, affordable”
- “Vegetarian restaurant with great atmosphere in central Moscow”
- “Coffee shop with amazing desserts and outdoor seating in Kyiv”

The bot will call the API and return a beautifully formatted list of venues with name, cuisine, why it’s worth visiting, and address hint.

### 🛠 Tech Stack

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Aiogram](https://img.shields.io/badge/Aiogram-3.x-3776AB?logo=telegram&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-backend-009688?logo=fastapi&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google_Gemini-AI-8E75B2?logo=google&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-optional-FF6F91?logo=pydantic&logoColor=white)
![httpx](https://img.shields.io/badge/httpx%20%2F%20aiohttp-API%20client-4B8BBE)

### 🔜 Roadmap

- Inline buttons with photos and maps
- User preference saving
- Voice message support
- Tests and CI/CD
- Deployment on Render / Fly.io with webhook

### 🤝 Contributing

Contributions are welcome! Feel free to open issues and pull requests.

### 📄 License

MIT © unknxwnwxrld

⭐ If you find this project useful — give it a star!

Related project:  
- Backend API: https://github.com/unknxwnwxrld/hangouthunter-api
