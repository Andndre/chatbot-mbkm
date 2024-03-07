import os
from telegram.ext import ApplicationBuilder, CommandHandler
from src.commands.hello import hello
from dotenv import load_dotenv

load_dotenv()

app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
app.add_handler(CommandHandler("hello", hello))
