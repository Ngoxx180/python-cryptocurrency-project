# Coinmarketcap - This script returns a paginated list of all active cryptocurrencies with latest market data.
import requests

# https://coinmarketcap.com/api/documentation/v1/#section/Quick-Start-Guide
# https://coinmarketcap.com/api/documentation/v1/#operation/getV2CryptocurrencyOhlcvHistorical
# Latest lists of all coins from coinmarketcap api key

cmc_listings_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
# Limit the data returned to first 20 cryptocurrencies using query parameters

parameters = {
    "start": "1",
    "limit": "10",
    "convert": "USD",
    "sort": "market_cap_by_total_supply_strict",
    "sort": "market_cap_strict",
}

headers = {
    "Accepts": "application/json",
    #"X-CMC_PRO_API_KEY": "00262ed9-c562-4378-b9e6-efeff1b62b97",
    "X-CMC_PRO_API_KEY": "SECRET_KEY"
}

response = requests.get(cmc_listings_url, headers=headers, params=parameters)
# Convert the json payload to a python data type

# Need to print .json() bc response doesn't have a get method. Need to use json to get actual data
print(response.json())


"""
+++++++++++++++++++++++++++++
3/8/21
(X)QUESTION: How do I input a coin that I want to view- How to view coin named "Harmony"?
             The ID is 3945, but I can't figure out how to put id in the parameter?

    Hypothesis: Maybe I have the wrong url calling..?
                I looked at the other calls and turns out there is Quotes/Latest and that has id in the paramters..

    Answer:     Created a new file called quotes-cmc.py where the url calling is
                'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
                The id parameter works!
    Lesson Learned: Read the documentation, get a general understanding of the content. Then know what to find before carelessly
                    attempting.
                    My keyword was "ID", but that wasn't in the https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest
                    so then I kept scrolling in the docs and found "id" in https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest

(X)QUESTION: on https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsLatest
            What does sort against ... mean?
            What is the difference between that and the parameter-
            why can't I put that the sort against, specifically "symbol" in the parameter?
    Answer: Sort is the parameter, the items in that 'sort against' list are the values you can use.
            The values in the list are 'sortable' -eg they have values that can be compared in logical ways
            to other values of the same data type

Next steps:
- Implement Environment variables (hide api key)
- Implement Prometheus metrics

Optional steps:
- Create a list of cryptocurrencies for user to select from
"""
