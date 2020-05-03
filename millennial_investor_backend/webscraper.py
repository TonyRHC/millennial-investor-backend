import requests
from bs4 import BeautifulSoup

FUTURES_URL = "https://finance.yahoo.com/commodities"
GOOGLE_NEWS_URL = "https://news.google.com/news?q={}&output=rss"
STOCKS_URL = "https://finance.yahoo.com/quote/{}?p={}&.tsrc=fin-srch"

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

def get_headliners(keyword):
    page = requests.get(GOOGLE_NEWS_URL.format(keyword))
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.select('title')
    descript = soup.select('description')
    pubdate = soup.select('pubdate')

    titleList = []
    hrefList = []
    pubdateList = []

    for i in range(1, len(descript)-1):
        temp = BeautifulSoup(descript[i].get_text(), 'html.parser')

        titleList.append(title[i].get_text().replace('&apos;',''))  # Cleans up description
        hrefList.append(temp.select('a')[0]['href'])
        pubdateList.append(pubdate[i-1].get_text())

    headliners = []
    for i in range(len(titleList)):
        headliner = {
            'title': titleList[i],
            'link': hrefList[i],
            'pubdate': pubdateList[i]
        }
        headliners.append(headliner)
    
    return headliners

def get_stock(symbol):
    page = requests.get(STOCKS_URL.format(symbol, symbol))
    soup = BeautifulSoup(page.content, 'html.parser')
    if soup.find('h2') != None:
        return None
    
    data = soup.find('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})
    price = data.find('span').text
    change = data.find_all('span')[1].text
    return {
        'symbol': symbol,
        'price': price,
        'change': change 
    }