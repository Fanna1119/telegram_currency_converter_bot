from telegram import Update
from telegram.ext import ContextTypes
from currency_symbols import CurrencySymbols
from .cache_request import convert_from_to
from locales.currencies import currencies
from helpers.helpers import validate_currency_input
from messages.messages import convert_usage, invalid_currency


def convert_base(from_currency, to_currency, amount):
    # get the data
    data = convert_from_to(from_currency, to_currency, float(amount))

    rounded_data = round(data, 2)

    # get the currency symbol
    symbol_one = CurrencySymbols.get_symbol(from_currency)
    symbol_two = CurrencySymbols.get_symbol(to_currency)

    response = f"{symbol_one}{amount} = {symbol_two}{rounded_data}"

    return response


async def convert(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

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

    response = convert_base(from_currency, to_currency, amount)

    await update.message.reply_text(response)
