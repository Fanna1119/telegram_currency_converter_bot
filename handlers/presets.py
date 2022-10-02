from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from db_config import add_preset, get_presets
from helpers.helpers import validate_currency_input
from messages.messages import convert_usage, invalid_currency
from .inline_keyboards import preset_keyboard

async def create_preset(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    try:
        from_currency = context.args[0].upper()
        to_currency = context.args[1].upper()
        amount = context.args[2]
    except IndexError:
        await update.message.reply_text(convert_usage)
        return

    if (validate_currency_input(from_currency, to_currency) == False):
        await update.message.reply_text(invalid_currency)
        return

    user_id = update.message.from_user.id
    preset = f"{from_currency} {to_currency} {amount}"
    add_preset(user_id, preset)
    await update.message.reply_text(f"preset created: {preset}, use /presets to retrieve it")


async def retrieve_presets(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    user_id = update.message.from_user.id
    presets = get_presets(user_id)

    reply_markup = preset_keyboard(presets, 'get')

    await update.message.reply_text('Please choose a preset:', reply_markup=reply_markup)


async def delete_preset(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    presets = get_presets(user_id)

    reply_markup = preset_keyboard(presets, 'delete')

    await update.message.reply_text('Please choose a preset to delete:', reply_markup=reply_markup)


