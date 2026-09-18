from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8935973793:AAHBW6VzoZPLV4rxbGJcY_hJstAnfcxk8ms"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! 👋 من بات تو هستم.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("بات روشن شد! ✅")
app.run_polling()
