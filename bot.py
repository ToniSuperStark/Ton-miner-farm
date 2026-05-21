import os
import requests
from dotenv import load_dotenv
from flask import Flask, request

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://ton-miner-farm.onrender.com")

app = Flask(__name__)

def send_message(chat_id, text, reply_markup=None):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "HTML"}
    if reply_markup:
        payload["reply_markup"] = reply_markup
    requests.post(url, json=payload)

@app.route(f"/webhook/{BOT_TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()
    if data and "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        
        if text == "/start":
            keyboard = {
                "inline_keyboard": [[{
                    "text": "🚀 Открыть ферму",
                    "web_app": {"url": WEBAPP_URL}
                }]]
            }
            send_message(chat_id, "Добро пожаловать в TON Miner Farm!", keyboard)
    return "ok"

@app.route("/")
def index():
    return "TON Farm Bot is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
