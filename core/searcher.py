import requests
from bs4 import BeautifulSoup

def get_page_health(target_content, fake_content):
    if not target_content or not fake_content:
        return False
    
    if abs(len(target_content) - len(fake_content)) < 800:
        return False

    return True

def get_page_contents(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

    page = requests.get(url, headers=headers)

    if page.status_code == 200:
        return page.text

    return None

def get_page_raw_contents(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

    page = requests.get(url, headers=headers)

    return page.text

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


def clean(text):
    return " ".join(text.replace("\xa0", " ").split())

def get_product_data(page_contents):
    soup = BeautifulSoup(page_contents, 'html.parser')

    container = soup.select_one("div.summary.entry-summary")
    if not container:
        return None

    title = container.select_one("h1.product_title")
    price = container.select_one("span.woocommerce-Price-amount")

    result = {
        "title": title.get_text(strip=True) if title else None,
        "price": price.get_text(strip=True) if price else None,
        "mangaka": None,
        "contenido": None,
        "editorial": None,
        "editorial_original": None,
        "formato": None,
        "isbn": None
    }

    desc = soup.select_one("div.woocommerce-product-details__short-description")

    if not desc:
        return result

    tags = desc.find_all(["strong", "b"])

    for tag in tags:
        key = clean(tag.get_text()).lower().replace(":", "")

        value = ""
        for sibling in tag.next_siblings:
            if sibling.name in ["strong", "b"]:
                break
            if isinstance(sibling, str):
                value += sibling
            else:
                value += sibling.get_text(" ", strip=True)

        value = clean(value)

        key = key.replace("\xa0", " ").strip()

        if "mangaka" in key:
            result["mangaka"] = value
        elif "contenido" in key:
            result["contenido"] = value
        elif "editorial original" in key:
            result["editorial_original"] = value
        elif "editorial" in key:
            result["editorial"] = value
        elif "formato" in key:
            result["formato"] = value
        elif "isbn" in key:
            result["isbn"] = value

    return result