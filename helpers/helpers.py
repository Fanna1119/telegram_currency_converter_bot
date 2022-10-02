from locales.currencies import currencies


def remove_duplicates(data):
    return list(set(data))


def validate_currency(currency):
    return currency.upper() in currencies


def validate_currency_input(currency_one, currency_two):
    if (currency_one not in currencies or currency_two not in currencies):
        return False
