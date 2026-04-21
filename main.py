import core.searcher as searcher
import core.writter as writter
import core.data as data
import core.processor as proccessor

def is_valid_page(page_contents):
    return page_contents and searcher.get_page_health(page_contents, data.get_fake_content())

def get_publishers(url):    
    print('Searching publishers in ' + url)
    page_contents = searcher.get_page_contents(url)
    
    if not is_valid_page(page_contents):
        print("Web not found:", url)
        return
    
    if page_contents:
        publishers_urls = searcher.get_publisher_urls(page_contents)

        for pub_url in publishers_urls:
            for comb_url in proccessor.GetCombinationFromStrip(proccessor.GetStripURL(pub_url), proccessor.GetBaseURL(pub_url)):
                data.add_publisher(comb_url)
    else:
        print('Failed to get publishers.')


def get_series(url):
    print('Searching series in ' + url)
    page_contents = searcher.get_page_contents(url)
    
    if not is_valid_page(page_contents):
        print("Web not found:", url)
        return

    if page_contents:
        series_urls = searcher.get_series_urls(page_contents)
        highlighted_series_urls = searcher.get_highlighted_series_urls(page_contents)

        for s_url in series_urls:
            data.add_series(s_url)
            
        for h_url in highlighted_series_urls:
            data.add_series(h_url)
    else:
        print('Failed to get series. In ' + url)
        
def get_products(url):    
    print('Searching products in ' + url)
    page_contents = searcher.get_page_contents(url)
    
    if not is_valid_page(page_contents):
        print("Web not found:", url)
        return
    
    if page_contents:
        products_urls = searcher.get_products_urls(page_contents)

        for s_url in products_urls:
            data.add_products(s_url)
    else:
        print('Failed to get products. In ' + url)
        
def get_product_data(url):    
    print('Searching product data in ' + url)
    page_contents = searcher.get_page_contents(url)
    
    if not is_valid_page(page_contents):
        print("Web not found:", url)
        return 
    
    if page_contents:
        data_cluster = searcher.get_product_data(page_contents)
        #print(data_cluster)

        for pd in data_cluster:
            print(f"{pd}: {data_cluster[pd]}")
    else:
        print('Failed to get products. In ' + url)


if __name__ == '__main__':
    writter.init()

    data.clear_all()
    data.set_fake_content(searcher.get_page_raw_contents('https://nubecomics.com/fake-url-123456789-aaa'))
    
    if(False):
        print("Start")
        if(True):
            get_publishers("https://nubecomics.com/mangas/")
        
            writter.clear_file("results/publishers.txt")
            writter.save_to_txt("results/publishers.txt", data.get_publishers())

            for pub_url in data.get_publishers():
                get_series(pub_url)
            
            writter.clear_file("results/series.txt")
            writter.save_to_txt("results/series.txt", data.get_series())
        else:
            data.found_publishers = writter.load_from_txt("results/publishers.txt")
            data.found_series = writter.load_from_txt("results/series.txt")
        

    
    
        for pub_url in data.get_publishers():
            get_products(pub_url)

        for series_url in data.get_series():
            get_products(series_url)
    
        writter.clear_file("results/products.txt")
        writter.save_to_txt("results/products.txt", data.get_products())
    get_product_data("https://nubecomics.com/producto/20th-century-boys-vol-01/")
    