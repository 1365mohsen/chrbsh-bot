from flask import Flask
import threading
import bot

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is Running!"

def run_bot():
    bot.main()

if name == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=8080)
