import requests
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0'
}

def get_page_contents(url):
    try:
        res = requests.get(url, headers=HEADERS)
        if res.status_code == 200:
            return res.text
    except:
        pass
    return None

def get_publisher_urls(page_contents):
    soup = BeautifulSoup(page_contents, 'html.parser')
    items = soup.find_all('a', class_='uael-grid-img')

    urls = []

    for item in items:
        link = item.get('href')
        if link:
            urls.append(link)

    return urls

def get_series_urls(page_contents):
    soup = BeautifulSoup(page_contents, 'html.parser')
    items = soup.find_all('a', class_='uael-grid-img')

    urls = []

    for item in items:
        link = item.get('href')
        if link:
            urls.append(link)

    return urls


def get_highlighted_series_urls(page_contents):
    soup = BeautifulSoup(page_contents, 'html.parser')
    items = soup.find_all('a', class_='uael-grid-img')

    urls = []

    for item in items:
        link = item.get('href')
        if link:
            urls.append(link)

    return urls