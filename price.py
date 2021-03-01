import requests

# https://coinmarketcap.com/api/documentation/v1/#section/Quick-Start-Guide
# Latest lists of all coins from coinmarketcap sandbox instance

cmc_listings_url = (
    "https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
)
# Limit the data returned to first 20 cryptocurrencies using query parameters
parameters = {"start": "1", "limit": "20", "convert": "USD"}
# Pass the required API key
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": "b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c",
}
# Call the API endpoint and pass parameters and header information
response = requests.get(cmc_listings_url, headers=headers, params=parameters)
# Convert the json payload to a python data type
response_json = response.json()
type(response_json)
# Let's explore the response
response_json
# That's a lot of data, what top level keys are there?
response_json.keys()
# Data probably has what we are looking for, let's look at just that:
response_json["data"]
# Better but let's see if we can narrow that down:
response_json["data"].keys()
# Doh, why are there no keys?
type(response_json["data"])
# Display the information for the first item in the list:
response_json["data"][0]
# Loop through all the items in the list and print the name:
for coin in response_json["data"]:
    print(coin["name"])
