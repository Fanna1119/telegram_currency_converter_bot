from db_config import create_user
from telegram import Update
from telegram.ext import ContextTypes
from telegram import Update


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:


    user_id = update.message.from_user.id
    create_user(user_id)

    await update.message.reply_text(""" 
    commands:
    /currencies - list of available currencies
    /convert - convert currencies,  usage: /convert <from> <to> <amount>
    /presets - list of preset conversions
    /create - create a preset conversion
    /delete - delete a preset conversion
    /info - info about the bot
    """)

