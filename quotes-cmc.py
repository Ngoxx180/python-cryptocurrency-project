# Coinmarketcap- This script utilizes the /quotes/latest to returns the latest market quote for 1 or more cryptocurrencies
import requests
# for api

import json
# for jq module
# To show jq output -> python <python-file.py> | jq .
import logging
import time
from datetime import datetime, timedelta
from prometheus_client import start_http_server, Guage, Counter, Enum

from decouple import config
# for env vars
# https://pypi.org/project/python-decouple/#why-not-just-use-environment-variables


cmc_listings_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
# Limit the data returned to first 20 cryptocurrencies using query parameters

SECRET_KEY = config("API_KEY", default="No Key Found", cast=str)

parameters = {
    # "id": 3945,
    "slug": "ethereum,harmony,bitcoin"
}

headers = {"Accepts": "application/json", "X-CMC_PRO_API_KEY": SECRET_KEY}

response = requests.get(cmc_listings_url, headers=headers, params=parameters)
# Convert the json payload to a python data type

print(json.dumps((response.json())))
# Need to print .json() bc response doesn't have a get method. Need to use json to get actual data

# To print jq python [app] | jq .
# To use jq print(json.dumps(thingy)) to


"""
++++++++++++++++++++++++++
QUESTION: How to view multiple coins?
    Answer: instead of using the "id" paramter (for a single cryptocurrency),
            use slug (Alternatively pass a comma-separated list of cryptocurrency slugs.
                     [Example: "bitcoin,ethereum"])
"""
