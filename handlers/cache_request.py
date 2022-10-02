from datetime import timedelta
from requests_cache import CachedSession

session = CachedSession(
    'demo_cache',
    use_cache_dir=True,                # Save files in the default user cache dir
    cache_control=True,                # Use Cache-Control response headers for expiration, if available
    expire_after=timedelta(hours=4),    # Otherwise expire responses after one day
    allowable_codes=[200, 400],        # Cache 400 responses as a solemn reminder of your failures
    allowable_methods=['GET'], # Cache whatever HTTP methods you want
    ignored_parameters=['api_key'],    # Don't match this request param, and redact if from the cache
    match_headers=['Accept-Language'], # Cache a different response per language
    stale_if_error=True,               # In case of request errors, use stale cache data if possible
)


def get_currencies(currency):
    response = session.get(f"https://open.er-api.com/v6/latest/{currency}")
    return response.json()


def convert_from_to(from_currency, to_currency, amount):
    # get the data
    data = get_currencies(from_currency)

    # get the rate
    rate = data["rates"][to_currency]

    # calculate the amount
    amount = amount * rate

    # return the amount
    return amount
