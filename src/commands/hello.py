from telegram import Update
from telegram.ext import ContextTypes

from src.utils.time import salam_pembuka

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
	## Command '/hello'
 
	Mengirimkan pesan 'Halo <nama pengguna>! Selamat <waktu>!'
    """
    await update.message.reply_text(f"Halo {update.effective_user.first_name}! {salam_pembuka()}")
