from time import time
import robin_stocks.robinhood as r
from decouple import config
import time


def algo_trading_test():
    login = r.login(config('USERNAME'), config('PASSWORD'))

    while True:
        price = r.stocks.get_latest_price('BBBY', includeExtendedHours=True)
        time.sleep(1)
        print(price)


if __name__ == "__main__":
    algo_trading_test()
