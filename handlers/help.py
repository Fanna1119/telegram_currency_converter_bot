from telegram import Update
from telegram.ext import ContextTypes
from options import available_currencies


async def list_currencies(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    for i in available_currencies():
        await update.message.reply_text('\n'.join(i))
