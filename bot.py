
from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get('message', 'No message provided')

    if TELEGRAM_TOKEN and TELEGRAM_CHAT_ID:
        send_text = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {'chat_id': TELEGRAM_CHAT_ID, 'text': message}
        response = requests.post(send_text, data=payload)
        return {'status': 'sent', 'telegram_response': response.json()}, 200
    else:
        return {'status': 'error', 'message': 'Missing TELEGRAM_TOKEN or TELEGRAM_CHAT_ID'}, 500

@app.route('/')
def home():
    return 'Telegram Bot is Live!', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
