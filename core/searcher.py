import requests
from bs4 import BeautifulSoup

def get_page_contents(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

    page = requests.get(url, headers=headers)

    if page.status_code == 200:
        return page.text

    return None

def get_publisher_urls(page_contents):
    soup = BeautifulSoup(page_contents, 'html.parser')
    
    items = soup.select('a.e-gallery-item')

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

def get_products_urls(page_contents):
    soup = BeautifulSoup(page_contents, 'html.parser')
    items = soup.find_all('a', class_='woocommerce-LoopProduct-link')

    urls = []

    for item in items:
        link = item.get('href')
        if link:
            urls.append(link)

    return urls