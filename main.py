import core.searcher as searcher
import core.writter as writter
import core.data as data


def get_publishers(url):
    page_contents = searcher.get_page_contents(url)
    
    if page_contents:
        publishers_urls = searcher.get_publisher_urls(page_contents)

        for pub_url in publishers_urls:
            data.add_publisher(pub_url)
    else:
        print('Failed to get publishers.')


def get_series(url):
    page_contents = searcher.get_page_contents(url)

    if page_contents:
        series_urls = searcher.get_series_urls(page_contents)
        highlighted_series_urls = searcher.get_highlighted_series_urls(page_contents)

        for s_url in series_urls:
            data.add_url(s_url)
            
        for h_url in highlighted_series_urls:
            data.add_url(h_url)
    else:
        print('Failed to get series. In ' + url)


if __name__ == '__main__':
    
    writter.init()

    data.clear_all()

    get_publishers("https://nubecomics.com/mangas/")

    for pub_url in data.get_publishers():
        get_series(pub_url)

    writter.clear_file("results/publishers.txt")
    writter.save_to_txt("results/publishers.txt", data.get_publishers())
    
    writter.clear_file("results/series.txt")
    writter.save_to_txt("results/series.txt", data.get_urls())