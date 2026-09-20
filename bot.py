from telegram.ext import Application, CommandHandler

TOKEN = "8848048833:AAFVzV0_Hxi4jSvBrEiKDmHkBNEAZCmaRa8"

async def start(update, context):
    await update.message.reply_text("ربات روشنه ✅\nبگو چی سرچ کنم؟")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("ربات روشن شد...")
app.run_polling()