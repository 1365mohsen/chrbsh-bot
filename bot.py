import os
from telegram.ext import Application, CommandHandler
from telegram.request import HTTPXRequest

# توکن رو از متغیر محیطی میخونه، اگه نبود همون قبلی
TOKEN = os.getenv("BOT_TOKEN", "8848048833:AAFVzV0_Hxi4jSvBrEiKDmHkBNEAZCmaRa8")

async def start(update, context):
    await update.message.reply_text("ربات روشنه ✅\nبگو چی سرچ کنم؟")

def main():
    # پروکسی برای دور زدن فیلترینگ پارس‌پک
    # پارس‌پک خودش اگه پروکسی خروج رو فعال کنی نیاز به این نداره
    # ولی این کد هر دو حالت رو ساپورت میکنه
    proxy_url = os.getenv("HTTP_PROXY") or os.getenv("HTTPS_PROXY") or "http://89.110.53.123:8080"
    
    request = HTTPXRequest(
        proxy=proxy_url,
        connect_timeout=20.0,
        read_timeout=30.0
    )
    
    app = Application.builder().token(TOKEN).request(request).build()
    app.add_handler(CommandHandler("start", start))

    print("ربات روشن شد...")
    app.run_polling()

if name == "main":
    main()
