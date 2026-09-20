from flask import Flask
import threading
import bot

app = Flask(name)

@app.route('/')
def home():
    return "Bot is Running!"

def run_bot():
    bot.main()

if name == "main":
    threading.Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=8080
