import requests
from bs4 import BeautifulSoup

FUTURES_URL = "https://finance.yahoo.com/commodities"

def get_futures():
    page = requests.get(FUTURES_URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    symbols = []
    names = []
    prices = []
    changes = []
    percentChanges = []
    volumes = []

    for listing in soup.find_all('tr'):
        for symbol in listing.find_all('td', attrs={'class': 'data-col0'}):
            symbols.append(symbol.text)
        for name in listing.find_all('td', attrs={'class': 'data-col1'}):
            names.append(name.text)
        for price in listing.find_all('td', attrs={'class': 'data-col2'}):
            prices.append(price.text)
        for change in listing.find_all('td', attrs={'class': 'data-col4'}):
            changes.append(change.text)
        for percentChange in listing.find_all('td', attrs={'class': 'data-col5'}):
            percentChanges.append(percentChange.text)
        for volume in listing.find_all('td', attrs={'class': 'data-col6'}):
            volumes.append(volume.text)

    futures = []
    for i in range(len(symbols)):
        future = {
            'symbol': symbols[i],
            'name': names[i],
            'price' : prices[i],
            'change': changes[i],
            'percentChange': percentChanges[i],
            'volume': volumes[i]
        }
        futures.append(future)

    return futures