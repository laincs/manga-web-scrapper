found_publishers = set()
found_series = set()
found_products = set()
found_final_data = set()

fake_content = set()

def set_fake_content(new_content):
    fake_content.add(new_content)
    
def get_fake_content():
    return list(fake_content)[0]

def add_final_data(url):
    global found_final_data
    if url:
        found_final_data.add(url)

def get_final_data():
    return list(found_final_data)

def clear_final_data():
    global found_final_data
    found_final_data.clear()

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