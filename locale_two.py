import pycountry

locales = [
    {
        "currency_code": "AED",
        "currency_name": "UAE Dirham",
        "Country": "United Arab Emirates"
    },
    {
        "currency_code": "AFN",
        "currency_name": "Afghan Afghani",
        "Country": "Afghanistan"
    },
    {
        "currency_code": "ALL",
        "currency_name": "Albanian Lek",
        "Country": "Albania"
    },
    {
        "currency_code": "AMD",
        "currency_name": "Armenian Dram",
        "Country": "Armenia"
    },
    {
        "currency_code": "ANG",
        "currency_name": "Netherlands Antillian Guilder",
        "Country": "Netherlands Antilles"
    },
    {
        "currency_code": "AOA",
        "currency_name": "Angolan Kwanza",
        "Country": "Angola"
    },
    {
        "currency_code": "ARS",
        "currency_name": "Argentine Peso",
        "Country": "Argentina"
    },
    {
        "currency_code": "AUD",
        "currency_name": "Australian Dollar",
        "Country": "Australia"
    },
    {
        "currency_code": "AWG",
        "currency_name": "Aruban Florin",
        "Country": "Aruba"
    },
    {
        "currency_code": "AZN",
        "currency_name": "Azerbaijani Manat",
        "Country": "Azerbaijan"
    },
    {
        "currency_code": "BAM",
        "currency_name": "Bosnia and Herzegovina Mark",
        "Country": "Bosnia and Herzegovina"
    },
    {
        "currency_code": "BBD",
        "currency_name": "Barbados Dollar",
        "Country": "Barbados"
    },
    {
        "currency_code": "BDT",
        "currency_name": "Bangladeshi Taka",
        "Country": "Bangladesh"
    },
    {
        "currency_code": "BGN",
        "currency_name": "Bulgarian Lev",
        "Country": "Bulgaria"
    },
    {
        "currency_code": "BHD",
        "currency_name": "Bahraini Dinar",
        "Country": "Bahrain"
    },
    {
        "currency_code": "BIF",
        "currency_name": "Burundian Franc",
        "Country": "Burundi"
    },
    {
        "currency_code": "BMD",
        "currency_name": "Bermudian Dollar",
        "Country": "Bermuda"
    },
    {
        "currency_code": "BND",
        "currency_name": "Brunei Dollar",
        "Country": "Brunei"
    },
    {
        "currency_code": "BOB",
        "currency_name": "Bolivian Boliviano",
        "Country": "Bolivia"
    },
    {
        "currency_code": "BRL",
        "currency_name": "Brazilian Real",
        "Country": "Brazil"
    },
    {
        "currency_code": "BSD",
        "currency_name": "Bahamian Dollar",
        "Country": "Bahamas"
    },
    {
        "currency_code": "BTN",
        "currency_name": "Bhutanese Ngultrum",
        "Country": "Bhutan"
    },
    {
        "currency_code": "BWP",
        "currency_name": "Botswana Pula",
        "Country": "Botswana"
    },
    {
        "currency_code": "BYN",
        "currency_name": "Belarusian Ruble",
        "Country": "Belarus"
    },
    {
        "currency_code": "BZD",
        "currency_name": "Belize Dollar",
        "Country": "Belize"
    },
    {
        "currency_code": "CAD",
        "currency_name": "Canadian Dollar",
        "Country": "Canada"
    },
    {
        "currency_code": "CDF",
        "currency_name": "Congolese Franc",
        "Country": "Democratic Republic of the Congo"
    },
    {
        "currency_code": "CHF",
        "currency_name": "Swiss Franc",
        "Country": "Switzerland"
    },
    {
        "currency_code": "CLP",
        "currency_name": "Chilean Peso",
        "Country": "Chile"
    },
    {
        "currency_code": "CNY",
        "currency_name": "Chinese Renminbi",
        "Country": "China"
    },
    {
        "currency_code": "COP",
        "currency_name": "Colombian Peso",
        "Country": "Colombia"
    },
    {
        "currency_code": "CRC",
        "currency_name": "Costa Rican Colon",
        "Country": "Costa Rica"
    },
    {
        "currency_code": "CUP",
        "currency_name": "Cuban Peso",
        "Country": "Cuba"
    },
    {
        "currency_code": "CVE",
        "currency_name": "Cape Verdean Escudo",
        "Country": "Cape Verde"
    },
    {
        "currency_code": "CZK",
        "currency_name": "Czech Koruna",
        "Country": "Czech Republic"
    },
    {
        "currency_code": "DJF",
        "currency_name": "Djiboutian Franc",
        "Country": "Djibouti"
    },
    {
        "currency_code": "DKK",
        "currency_name": "Danish Krone",
        "Country": "Denmark"
    },
    {
        "currency_code": "DOP",
        "currency_name": "Dominican Peso",
        "Country": "Dominican Republic"
    },
    {
        "currency_code": "DZD",
        "currency_name": "Algerian Dinar",
        "Country": "Algeria"
    },
    {
        "currency_code": "EGP",
        "currency_name": "Egyptian Pound",
        "Country": "Egypt"
    },
    {
        "currency_code": "ERN",
        "currency_name": "Eritrean Nakfa",
        "Country": "Eritrea"
    },
    {
        "currency_code": "ETB",
        "currency_name": "Ethiopian Birr",
        "Country": "Ethiopia"
    },
    {
        "currency_code": "EUR",
        "currency_name": "Euro",
        "Country": "European Union"
    },
    {
        "currency_code": "FJD",
        "currency_name": "Fiji Dollar",
        "Country": "Fiji"
    },
    {
        "currency_code": "FKP",
        "currency_name": "Falkland Islands Pound",
        "Country": "Falkland Islands"
    },
    {
        "currency_code": "FOK",
        "currency_name": "Faroese Króna",
        "Country": "Faroe Islands"
    },
    {
        "currency_code": "GBP",
        "currency_name": "Pound Sterling",
        "Country": "United Kingdom"
    },
    {
        "currency_code": "GEL",
        "currency_name": "Georgian Lari",
        "Country": "Georgia"
    },
    {
        "currency_code": "GGP",
        "currency_name": "Guernsey Pound",
        "Country": "Guernsey"
    },
    {
        "currency_code": "GHS",
        "currency_name": "Ghanaian Cedi",
        "Country": "Ghana"
    },
    {
        "currency_code": "GIP",
        "currency_name": "Gibraltar Pound",
        "Country": "Gibraltar"
    },
    {
        "currency_code": "GMD",
        "currency_name": "Gambian Dalasi",
        "Country": "The Gambia"
    },
    {
        "currency_code": "GNF",
        "currency_name": "Guinean Franc",
        "Country": "Guinea"
    },
    {
        "currency_code": "GTQ",
        "currency_name": "Guatemalan Quetzal",
        "Country": "Guatemala"
    },
    {
        "currency_code": "GYD",
        "currency_name": "Guyanese Dollar",
        "Country": "Guyana"
    },
    {
        "currency_code": "HKD",
        "currency_name": "Hong Kong Dollar",
        "Country": "Hong Kong"
    },
    {
        "currency_code": "HNL",
        "currency_name": "Honduran Lempira",
        "Country": "Honduras"
    },
    {
        "currency_code": "HRK",
        "currency_name": "Croatian Kuna",
        "Country": "Croatia"
    },
    {
        "currency_code": "HTG",
        "currency_name": "Haitian Gourde",
        "Country": "Haiti"
    },
    {
        "currency_code": "HUF",
        "currency_name": "Hungarian Forint",
        "Country": "Hungary"
    },
    {
        "currency_code": "IDR",
        "currency_name": "Indonesian Rupiah",
        "Country": "Indonesia"
    },
    {
        "currency_code": "ILS",
        "currency_name": "Israeli New Shekel",
        "Country": "Israel"
    },
    {
        "currency_code": "IMP",
        "currency_name": "Manx Pound",
        "Country": "Isle of Man"
    },
    {
        "currency_code": "INR",
        "currency_name": "Indian Rupee",
        "Country": "India"
    },
    {
        "currency_code": "IQD",
        "currency_name": "Iraqi Dinar",
        "Country": "Iraq"
    },
    {
        "currency_code": "IRR",
        "currency_name": "Iranian Rial",
        "Country": "Iran"
    },
    {
        "currency_code": "ISK",
        "currency_name": "Icelandic Króna",
        "Country": "Iceland"
    },
    {
        "currency_code": "JEP",
        "currency_name": "Jersey Pound",
        "Country": "Jersey"
    },
    {
        "currency_code": "JMD",
        "currency_name": "Jamaican Dollar",
        "Country": "Jamaica"
    },
    {
        "currency_code": "JOD",
        "currency_name": "Jordanian Dinar",
        "Country": "Jordan"
    },
    {
        "currency_code": "JPY",
        "currency_name": "Japanese Yen",
        "Country": "Japan"
    },
    {
        "currency_code": "KES",
        "currency_name": "Kenyan Shilling",
        "Country": "Kenya"
    },
    {
        "currency_code": "KGS",
        "currency_name": "Kyrgyzstani Som",
        "Country": "Kyrgyzstan"
    },
    {
        "currency_code": "KHR",
        "currency_name": "Cambodian Riel",
        "Country": "Cambodia"
    },
    {
        "currency_code": "KID",
        "currency_name": "Kiribati Dollar",
        "Country": "Kiribati"
    },
    {
        "currency_code": "KMF",
        "currency_name": "Comorian Franc",
        "Country": "Comoros"
    },
    {
        "currency_code": "KRW",
        "currency_name": "South Korean Won",
        "Country": "South Korea"
    },
    {
        "currency_code": "KWD",
        "currency_name": "Kuwaiti Dinar",
        "Country": "Kuwait"
    },
    {
        "currency_code": "KYD",
        "currency_name": "Cayman Islands Dollar",
        "Country": "Cayman Islands"
    },
    {
        "currency_code": "KZT",
        "currency_name": "Kazakhstani Tenge",
        "Country": "Kazakhstan"
    },
    {
        "currency_code": "LAK",
        "currency_name": "Lao Kip",
        "Country": "Laos"
    },
    {
        "currency_code": "LBP",
        "currency_name": "Lebanese Pound",
        "Country": "Lebanon"
    },
    {
        "currency_code": "LKR",
        "currency_name": "Sri Lanka Rupee",
        "Country": "Sri Lanka"
    },
    {
        "currency_code": "LRD",
        "currency_name": "Liberian Dollar",
        "Country": "Liberia"
    },
    {
        "currency_code": "LSL",
        "currency_name": "Lesotho Loti",
        "Country": "Lesotho"
    },
    {
        "currency_code": "LYD",
        "currency_name": "Libyan Dinar",
        "Country": "Libya"
    },
    {
        "currency_code": "MAD",
        "currency_name": "Moroccan Dirham",
        "Country": "Morocco"
    },
    {
        "currency_code": "MDL",
        "currency_name": "Moldovan Leu",
        "Country": "Moldova"
    },
    {
        "currency_code": "MGA",
        "currency_name": "Malagasy Ariary",
        "Country": "Madagascar"
    },
    {
        "currency_code": "MKD",
        "currency_name": "Macedonian Denar",
        "Country": "North Macedonia"
    },
    {
        "currency_code": "MMK",
        "currency_name": "Burmese Kyat",
        "Country": "Myanmar"
    },
    {
        "currency_code": "MNT",
        "currency_name": "Mongolian Tögrög",
        "Country": "Mongolia"
    },
    {
        "currency_code": "MOP",
        "currency_name": "Macanese Pataca",
        "Country": "Macau"
    },
    {
        "currency_code": "MRU",
        "currency_name": "Mauritanian Ouguiya",
        "Country": "Mauritania"
    },
    {
        "currency_code": "MUR",
        "currency_name": "Mauritian Rupee",
        "Country": "Mauritius"
    },
    {
        "currency_code": "MVR",
        "currency_name": "Maldivian Rufiyaa",
        "Country": "Maldives"
    },
    {
        "currency_code": "MWK",
        "currency_name": "Malawian Kwacha",
        "Country": "Malawi"
    },
    {
        "currency_code": "MXN",
        "currency_name": "Mexican Peso",
        "Country": "Mexico"
    },
    {
        "currency_code": "MYR",
        "currency_name": "Malaysian Ringgit",
        "Country": "Malaysia"
    },
    {
        "currency_code": "MZN",
        "currency_name": "Mozambican Metical",
        "Country": "Mozambique"
    },
    {
        "currency_code": "NAD",
        "currency_name": "Namibian Dollar",
        "Country": "Namibia"
    },
    {
        "currency_code": "NGN",
        "currency_name": "Nigerian Naira",
        "Country": "Nigeria"
    },
    {
        "currency_code": "NIO",
        "currency_name": "Nicaraguan Córdoba",
        "Country": "Nicaragua"
    },
    {
        "currency_code": "NOK",
        "currency_name": "Norwegian Krone",
        "Country": "Norway"
    },
    {
        "currency_code": "NPR",
        "currency_name": "Nepalese Rupee",
        "Country": "Nepal"
    },
    {
        "currency_code": "NZD",
        "currency_name": "New Zealand Dollar",
        "Country": "New Zealand"
    },
    {
        "currency_code": "OMR",
        "currency_name": "Omani Rial",
        "Country": "Oman"
    },
    {
        "currency_code": "PAB",
        "currency_name": "Panamanian Balboa",
        "Country": "Panama"
    },
    {
        "currency_code": "PEN",
        "currency_name": "Peruvian Sol",
        "Country": "Peru"
    },
    {
        "currency_code": "PGK",
        "currency_name": "Papua New Guinean Kina",
        "Country": "Papua New Guinea"
    },
    {
        "currency_code": "PHP",
        "currency_name": "Philippine Peso",
        "Country": "Philippines"
    },
    {
        "currency_code": "PKR",
        "currency_name": "Pakistani Rupee",
        "Country": "Pakistan"
    },
    {
        "currency_code": "PLN",
        "currency_name": "Polish Złoty",
        "Country": "Poland"
    },
    {
        "currency_code": "PYG",
        "currency_name": "Paraguayan Guaraní",
        "Country": "Paraguay"
    },
    {
        "currency_code": "QAR",
        "currency_name": "Qatari Riyal",
        "Country": "Qatar"
    },
    {
        "currency_code": "RON",
        "currency_name": "Romanian Leu",
        "Country": "Romania"
    },
    {
        "currency_code": "RSD",
        "currency_name": "Serbian Dinar",
        "Country": "Serbia"
    },
    {
        "currency_code": "RUB",
        "currency_name": "Russian Ruble",
        "Country": "Russia"
    },
    {
        "currency_code": "RWF",
        "currency_name": "Rwandan Franc",
        "Country": "Rwanda"
    },
    {
        "currency_code": "SAR",
        "currency_name": "Saudi Riyal",
        "Country": "Saudi Arabia"
    },
    {
        "currency_code": "SBD",
        "currency_name": "Solomon Islands Dollar",
        "Country": "Solomon Islands"
    },
    {
        "currency_code": "SCR",
        "currency_name": "Seychellois Rupee",
        "Country": "Seychelles"
    },
    {
        "currency_code": "SDG",
        "currency_name": "Sudanese Pound",
        "Country": "Sudan"
    },
    {
        "currency_code": "SEK",
        "currency_name": "Swedish Krona",
        "Country": "Sweden"
    },
    {
        "currency_code": "SGD",
        "currency_name": "Singapore Dollar",
        "Country": "Singapore"
    },
    {
        "currency_code": "SHP",
        "currency_name": "Saint Helena Pound",
        "Country": "Saint Helena"
    },
    {
        "currency_code": "SLE",
        "currency_name": "Sierra Leonean Leone",
        "Country": "Sierra Leone"
    },
    {
        "currency_code": "SOS",
        "currency_name": "Somali Shilling",
        "Country": "Somalia"
    },
    {
        "currency_code": "SRD",
        "currency_name": "Surinamese Dollar",
        "Country": "Suriname"
    },
    {
        "currency_code": "SSP",
        "currency_name": "South Sudanese Pound",
        "Country": "South Sudan"
    },
    {
        "currency_code": "STN",
        "currency_name": "São Tomé and Príncipe Dobra",
        "Country": "São Tomé and Príncipe"
    },
    {
        "currency_code": "SYP",
        "currency_name": "Syrian Pound",
        "Country": "Syria"
    },
    {
        "currency_code": "SZL",
        "currency_name": "Eswatini Lilangeni",
        "Country": "Eswatini"
    },
    {
        "currency_code": "THB",
        "currency_name": "Thai Baht",
        "Country": "Thailand"
    },
    {
        "currency_code": "TJS",
        "currency_name": "Tajikistani Somoni",
        "Country": "Tajikistan"
    },
    {
        "currency_code": "TMT",
        "currency_name": "Turkmenistan Manat",
        "Country": "Turkmenistan"
    },
    {
        "currency_code": "TND",
        "currency_name": "Tunisian Dinar",
        "Country": "Tunisia"
    },
    {
        "currency_code": "TOP",
        "currency_name": "Tongan Paʻanga",
        "Country": "Tonga"
    },
    {
        "currency_code": "TRY",
        "currency_name": "Turkish Lira",
        "Country": "Turkey"
    },
    {
        "currency_code": "TTD",
        "currency_name": "Trinidad and Tobago Dollar",
        "Country": "Trinidad and Tobago"
    },
    {
        "currency_code": "TVD",
        "currency_name": "Tuvaluan Dollar",
        "Country": "Tuvalu"
    },
    {
        "currency_code": "TWD",
        "currency_name": "New Taiwan Dollar",
        "Country": "Taiwan"
    },
    {
        "currency_code": "TZS",
        "currency_name": "Tanzanian Shilling",
        "Country": "Tanzania"
    },
    {
        "currency_code": "UAH",
        "currency_name": "Ukrainian Hryvnia",
        "Country": "Ukraine"
    },
    {
        "currency_code": "UGX",
        "currency_name": "Ugandan Shilling",
        "Country": "Uganda"
    },
    {
        "currency_code": "USD",
        "currency_name": "United States Dollar",
        "Country": "United States"
    },
    {
        "currency_code": "UYU",
        "currency_name": "Uruguayan Peso",
        "Country": "Uruguay"
    },
    {
        "currency_code": "UZS",
        "currency_name": "Uzbekistani So'm",
        "Country": "Uzbekistan"
    },
    {
        "currency_code": "VES",
        "currency_name": "Venezuelan Bolívar Soberano",
        "Country": "Venezuela"
    },
    {
        "currency_code": "VND",
        "currency_name": "Vietnamese Đồng",
        "Country": "Vietnam"
    },
    {
        "currency_code": "VUV",
        "currency_name": "Vanuatu Vatu",
        "Country": "Vanuatu"
    },
    {
        "currency_code": "WST",
        "currency_name": "Samoan Tālā",
        "Country": "Samoa"
    },
    {
        "currency_code": "XAF",
        "currency_name": "Central African CFA Franc",
        "Country": "CEMAC"
    },
    {
        "currency_code": "XCD",
        "currency_name": "East Caribbean Dollar",
        "Country": "Organisation of Eastern Caribbean States"
    },
    {
        "currency_code": "XDR",
        "currency_name": "Special Drawing Rights",
        "Country": "International Monetary Fund"
    },
    {
        "currency_code": "XOF",
        "currency_name": "West African CFA franc",
        "Country": "CFA"
    },
    {
        "currency_code": "XPF",
        "currency_name": "CFP Franc",
        "Country": "Collectivités d'Outre-Mer"
    },
    {
        "currency_code": "YER",
        "currency_name": "Yemeni Rial",
        "Country": "Yemen"
    },
    {
        "currency_code": "ZAR",
        "currency_name": "South African Rand",
        "Country": "South Africa"
    },
    {
        "currency_code": "ZMW",
        "currency_name": "Zambian Kwacha",
        "Country": "Zambia"
    },
    {
        "currency_code": "ZWL",
        "currency_name": "Zimbabwean Dollar",
        "Country": "Zimbabwe"
    }
]

# search Country
# def search_country(country):
#     for i in range(len(locales)):
#         if locales[i]["Country"] == country:
#             return locales[i]["currency_code"]
#     return "Not found"

    
# print(search_country("United States"))

# print(pycountry.countries.get(name="United States").alpha_2)

empty_list = {}

error_list = {}

for i in range(len(locales)):
    try:
        # print(pycountry.countries.get(name=locales[i]["Country"]).alpha_2)
        # construct = {
        #     pycountry.countries.get(name=locales[i]["Country"]).alpha_2: (locales[i]["currency_code"], locales[i]["currency_name"]),
        # }
        # empty_list.append(construct)
        empty_list[pycountry.countries.get(name=locales[i]["Country"]).alpha_2] = {
            "currency_code": locales[i]["currency_code"],
            "currency_name": locales[i]["currency_name"],
            "country": locales[i]["Country"],
            "locale_name": pycountry.countries.get(name=locales[i]["Country"]).alpha_2

        }
    except:

        error_list[locales[i]["Country"]] = {
            "currency_code": locales[i]["currency_code"],
            "currency_name": locales[i]["currency_name"],
            "country": locales[i]["Country"],
            "locale_name": "Not found"
        }


        # print(f"Not found: {locales[i]['Country']}")

    continue

print(error_list)

# print(empty_list)


# currency_code to list 
# def currency_code_to_list():
#     currency_code_list = []
#     for i in range(len(locales)):
#         currency_code_list.append(locales[i]["currency_code"])
#     return currency_code_list

# print(currency_code_to_list())

