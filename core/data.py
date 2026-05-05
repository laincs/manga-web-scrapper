class URLCluster():
    def __init__(self):
        self.data = {}
        
    def get_data(self):
        return list(self.data.values())
    
    def add_data(self, url):
        if (url):
            self.data[url]({
                "avalible" : True,
                "url" : url,
                "flag_publisher" : False,
                "flag_tags" : False,
                "flag_series" : False,
                "flag_products" : False,
                "flag_product_data" : False
            })
            
    def clear_data(self):
        self.data.clear()


cluster = URLCluster()
fake_content = set()