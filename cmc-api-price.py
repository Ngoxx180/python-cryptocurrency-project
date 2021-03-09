import requests

# https://coinmarketcap.com/api/documentation/v1/#section/Quick-Start-Guide
# https://coinmarketcap.com/api/documentation/v1/#operation/getV2CryptocurrencyOhlcvHistorical
# Latest lists of all coins from coinmarketcap api key

cmc_listings_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
# Limit the data returned to first 20 cryptocurrencies using query parameters

parameters = {
    "start": "1",
    "limit": "1",
    "convert": "USD",
    "sort": "market_cap_by_total_supply_strict",
    "sort": "market_cap_strict",
    "sort": "price"
    #"id":"3945" #ID doesn't work here, bc not part of paramters in docs. Maybe try in header?
}
# Pass the required API key

headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": "00262ed9-c562-4378-b9e6-efeff1b62b97",
}
# Call the API endpoint and pass parameters and header information

response = requests.get(cmc_listings_url, headers=headers, params=parameters)
# Convert the json payload to a python data type

#Need to print .json() bc response doesn't have a get method. Need to use json to get actual data
print(response.json())

"""Stuck..
QUESTION: How do I input a coin that I want to view- How to view coin named "Harmony"? The ID is 3945, but I can't figure out how to put id in the parameter?

QUESTION: on https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsLatest
What does sort against ... mean?
What is the difference between that and the parameter- why can't I put that the sort against, specifically "symbol" in the parameter?

"""

"""
Update.. Maybe I have the wrong url calling... I looked at the other calls and turns out there is Quotes/Latest and that has id in the paramters.. omg if this works..
Creating a new file called quotes-cmc.py

WOW... quotes-cmc.py works. I SPENT SO MUCH TIME TRYING TO FIGURE OUT THE ID PART IN THE PARAMETER..

Lesson learned:
- Reading documentation and knowing what to find before carelessly attempting to understand why something doesn't work.
    My keyword was "ID", but that wasn't in the https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest
    so then I kept scrolling in the docs and found "id" in https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest
"""

"""
Next steps:
-
"""
