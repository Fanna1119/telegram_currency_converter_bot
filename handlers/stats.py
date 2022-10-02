from .cache_request import get_currencies
from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime


def pretty_date(date):
    return datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = get_currencies('USD')
    # return data
    time_last_update_unix = pretty_date(data['time_last_update_unix'])
    time_next_update_unix = pretty_date(data['time_next_update_unix'])
    provider = data['provider']


    send_as_markdown = f"""
    *Last update:* {time_last_update_unix} \n
    *Next update:* {time_next_update_unix} \n
    *Provider:* {provider} \n
    *Developed by:* @fannala
    """

    await update.message.reply_markdown(send_as_markdown)
