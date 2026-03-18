found_publishers = set()
found_series = set()
found_urls = set()

def add_url(url):
    global found_urls
    if url:
        found_urls.add(url)

def get_urls():
    return list(found_urls)

def clear_urls():
    global found_urls
    found_urls.clear()

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
    clear_urls()
    clear_publishers()
    clear_series()