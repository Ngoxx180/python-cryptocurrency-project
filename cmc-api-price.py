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
    "sort": "market_cap_strict"
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
