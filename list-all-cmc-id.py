# This script lists all Coinmarketcap tokens

import requests

cmc_listings_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map"
# Limit the data returned to first 20 cryptocurrencies using query parameters

parameters = {
    "symbol": "ONE",
}

headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": "00262ed9-c562-4378-b9e6-efeff1b62b97",
}

response = requests.get(cmc_listings_url, headers=headers, params=parameters)

# Need to print .json() bc response doesn't have a get method. Need to use json to get actual data
print(response.json())

# Harmony "id":3945
# ETH: id 1027
