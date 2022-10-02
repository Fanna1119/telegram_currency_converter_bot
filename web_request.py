# # import http
# import http.client
# import json
# import flag
# import pycountry
# from currencies_locale import country_locales

# # funtion to get the data from the web and return json
# def get_currency_data(currency):
#     # create a connection
#     conn = http.client.HTTPSConnection("open.er-api.com")

#     # make a request
#     conn.request("GET", f"/v6/latest/{currency}")

#     # get the response
#     response = conn.getresponse()

#     # read the data
#     data = response.read()

#     # decode the data
#     data = data.decode("utf-8")

#     # convert the data to json
#     data = json.loads(data)

#     # return the data
#     return data


# # print(country_locales['AE']['country'])


# def convert_from_to(from_currency, to_currency, amount):
#     # get the data
#     data = get_currency_data(from_currency)

#     # get the rate
#     rate = data["rates"][to_currency]

#     # calculate the amount
#     amount = amount * rate

#     # return the amount
#     return amount

# # print(convert_from_to("USD", "ZAR", 1))