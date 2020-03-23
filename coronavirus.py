from bs4 import BeautifulSoup
import requests


def totalCases():
    r = requests.get('https://www.worldometers.info/coronavirus/')
    html_soup = BeautifulSoup(r.text, 'html.parser')
    totalCases = html_soup.find("div", class_="maincounter-number")
    totalCases = totalCases.find("span")
    totalCases = totalCases.string
    print(totalCases)
    return totalCases

def deaths():
    r = requests.get('https://www.worldometers.info/coronavirus/')
    html_soup = BeautifulSoup(r.text, 'html.parser')
    activeCases = html_soup.find_all("div", id="maincounter-wrap")
    activeCases = activeCases[1].find("span")
    activeCases = activeCases.string
    print(activeCases)
    return activeCases

def activeCases():
    r = requests.get('https://www.worldometers.info/coronavirus/')
    html_soup = BeautifulSoup(r.text, 'html.parser')
    casesactive = html_soup.find_all("div", id="maincounter-wrap")
    casesactive = casesactive[2].find("span")
    casesactive = casesactive.string
    print(casesactive)
    return casesactive
