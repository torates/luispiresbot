from bs4 import BeautifulSoup
import requests

r = requests.get('https://bitcoinwisdom.io/')

print(r.text)
