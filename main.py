from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os

load_dotenv()

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

if __name__ == "__main__":
	app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
	app.add_handler(CommandHandler("hello", hello))
	print('⚡ Bot is running!...')
	app.run_polling()
