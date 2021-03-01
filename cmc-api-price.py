import requests

# https://coinmarketcap.com/api/documentation/v1/#section/Quick-Start-Guide
# Latest lists of all coins from coinmarketcap sandbox instance

cmc_listings_url = (
    "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
)
# Limit the data returned to first 20 cryptocurrencies using query parameters

parameters = {"start": "1", "limit": "20", "convert": "USD"}
# Pass the required API key

headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": "00262ed9-c562-4378-b9e6-efeff1b62b97",
}
# Call the API endpoint and pass parameters and header information

response = requests.get(cmc_listings_url, headers=headers, params=parameters)
# Convert the json payload to a python data type
