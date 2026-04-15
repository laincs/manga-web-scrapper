found_publishers = set()
found_series = set()
found_products = set()

def add_products(url):
    global found_products
    if url:
        found_products.add(url)

def get_products():
    return list(found_products)

def clear_products():
    global found_products
    found_products.clear()

def add_publisher(publisher):
    global found_publishers
    if publisher:
        found_publishers.add(publisher)

def get_publishers():
    return list(found_publishers)

def clear_publishers():
    global found_publishers
    found_publishers.clear()

def add_series(series):
    global found_series
    if series:
        found_series.add(series)

def get_series():
    return list(found_series)

def clear_series():
    global found_series
    found_series.clear()

def clear_all():
    clear_products()
    clear_publishers()
    clear_series()