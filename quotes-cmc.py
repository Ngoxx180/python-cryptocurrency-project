import requests

# https://coinmarketcap.com/api/documentation/v1/#section/Quick-Start-Guide
# https://coinmarketcap.com/api/documentation/v1/#operation/getV2CryptocurrencyOhlcvHistorical
# Latest lists of all coins from coinmarketcap api key

cmc_listings_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
# Limit the data returned to first 20 cryptocurrencies using query parameters

parameters = {
    "id": "3945"
    #"id": "2" #this didn't work.. it showed LTC?
    #QUESTION: How to view multiple coins? 
}

headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": "00262ed9-c562-4378-b9e6-efeff1b62b97",
}

response = requests.get(cmc_listings_url, headers=headers, params=parameters)
# Convert the json payload to a python data type

#Need to print .json() bc response doesn't have a get method. Need to use json to get actual data
print(response.json())
