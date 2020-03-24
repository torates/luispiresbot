from bs4 import BeautifulSoup
import requests

class CoronaVirus:
    def totalCases():
        r = requests.get('https://www.worldometers.info/coronavirus/')
        html_soup = BeautifulSoup(r.text, 'html.parser')
        casestotal = html_soup.find("div", class_="maincounter-number")
        casestotal = casestotal.find("span")
        casestotal = casestotal.string
        return casestotal

    def deaths():
        r = requests.get('https://www.worldometers.info/coronavirus/')
        html_soup = BeautifulSoup(r.text, 'html.parser')
        perished = html_soup.find_all("div", id="maincounter-wrap")
        perished = perished[1].find("span")
        perished = perished.string
        return perished

    def activeCases():
        r = requests.get('https://www.worldometers.info/coronavirus/')
        html_soup = BeautifulSoup(r.text, 'html.parser')
        casesactive = html_soup.find_all("div", id="maincounter-wrap")
        casesactive = casesactive[2].find("span")
        casesactive = casesactive.string
        return casesactive
