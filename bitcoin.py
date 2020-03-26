from bs4 import BeautifulSoup
import requests


class BitcoinPrice:
    def coinbase():
        r = requests.get('https://bitcoinwisdom.io/markets/gdax/btcusd')
        html_soup = BeautifulSoup(r.text, 'html.parser')
        prices = html_soup.find("div", id='price')
        prices = prices.string
        print(prices)
        return prices
