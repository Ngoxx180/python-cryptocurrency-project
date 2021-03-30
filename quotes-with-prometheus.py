import requests
import json
import logging
import time
from datetime import datetime, timedelta
from prometheus_client import start_http_server, Gauge, Counter, Enum, Summary

from decouple import config

if __name__ == "__main__":
    counter = Counter('Request_num', 'Number of requests ran')
    req_summary = Summary('Request_duration', 'Duration of request')
    start_http_server(8089)

cmc_listings_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

SECRET_KEY = config("API_KEY", default="No Key Found", cast=str)

parameters = {
    "slug": "ethereum,harmony,0x"
    }

headers = {"Accepts": "application/json", "X-CMC_PRO_API_KEY": SECRET_KEY}
response = requests.get(cmc_listings_url, headers=headers, params=parameters)

print(json.dumps((response.json())))

# To print jq python [app] | jq .
# To use jq print(json.dumps(thingy)) to
