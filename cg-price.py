#This script utilizes CoinGecko's API calling 
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

while True:
    print('-----------------------------------------')
    print('\nWhat coin would you like to see? \nTo exit: "stop"\n')
    print('-----------------------------------------')

    coin = input()

    if coin == "exit":
        print("\nThank you, good bye")
        break

    print(
        cg.get_price(
            ids=coin,
            vs_currencies="usd",
            include_market_cap="true",
            include_24hr_change="true",
        )
    )
