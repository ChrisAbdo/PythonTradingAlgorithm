import robin_stocks.robinhood as r
from decouple import config
from termcolor import colored

separator = '----------------------------------------'


def algo_trading():
    print(separator)
    print(colored('Logging in...', 'green'))
    login = r.login(config('USERNAME'), config('PASSWORD'))
    print(login)
    print(colored('Logged in!', 'green'))
    print(separator)

    choice = input('Enter a stock ticker: $')
    print(separator)

    while True:
        price1 = r.stocks.get_latest_price(choice, includeExtendedHours=True)
        newPrice1 = price1[0]
        price2 = r.stocks.get_latest_price(choice, includeExtendedHours=True)
        newPrice2 = price2[0]

        if price1 > price2:
            print(colored('CURRENT: {}'.format(price1), 'blue') + '\t||' + colored('\tINC from {} to {}'.format(price2, price1), 'green') + '\t||' + colored('\t\u2191: {}%'.format(
                round(((float(newPrice1) - float(newPrice2)) / float(newPrice2)) * 100, 5)), 'green'))
            print(separator)

        elif price1 < price2:
            print(colored('CURRENT: {}'.format(price1), 'blue') + '\t||' + colored('\tDEC from {} to {}'.format(price2, price1), 'red') + '\t||' + colored('\t\u2193: {}%'.format(
                round(((float(newPrice1) - float(newPrice2)) / float(newPrice2)) * 100, 5)), 'red'))
            print(separator)


if __name__ == "__main__":
    algo_trading()
