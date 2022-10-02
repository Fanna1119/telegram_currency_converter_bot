import flag
from locales.currencies_locale import country_locales


def available_currencies():
    countries = []
    for country in country_locales:
        countries.append(
            f"{flag.flag(country)} | {country_locales[country]['country']} | {country_locales[country]['currency_code']} \n")
            
    countries = [countries[i:i + 20] for i in range(0, len(countries), 20)]

    return countries
