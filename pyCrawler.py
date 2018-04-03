"""
A very simple crawler implementation using Python 3.
"""

from LinkParser import LinkParser
from UrlProcessor import UrlProcessor

from pprint import pprint


class PyCrawler:
    def __init__(self, start_url, max_visited_pages=50):
        self.url_processor = UrlProcessor()
        if self.url_processor.check_if_valid_url(start_url):
            self.start_url = start_url
        else:
            raise Exception("Invalid Seed URL: {}".format(start_url))

        self.links = set()
        self.visited = dict()
        self.unvisited = list()
        if type(max_visited_pages) is int:
            self.MAX_VISITED_PAGES = max_visited_pages
        else:
            raise Exception("Invalid type for max_visited_pages")

    def filter_unvisited(self, links_set):
        result = set()
        for link in links_set:
            # If link not visited yet AND link not already in unvisited queue
            if link not in self.visited and link not in self.unvisited and self.url_processor.check_if_valid_url(link):
                result.add(link)
        return result

    def parse_url(self, url):
        url = url.rstrip("/")
        self.visited[url] = True
        self.unvisited.pop(0)
        parser = LinkParser(url)
        parser.get_all_links()
        return parser.links

    def crawler(self):
        curr_url = self.start_url
        self.unvisited.append(curr_url)

        while (len(self.visited) <= self.MAX_VISITED_PAGES) and len(self.unvisited):
            # print("Visited: ", len(self.visited), curr_url)
            # print("Length of final set: ", len(self.links))
            page_links = self.parse_url(curr_url)
            filtered_pages_links = self.filter_unvisited(page_links)

            self.unvisited += list(filtered_pages_links)
            self.links = self.links | filtered_pages_links

            if len(self.unvisited):
                curr_url = self.unvisited[0]


if __name__=="__main__":
    crawler = PyCrawler(start_url="https://www.python.org/", max_visited_pages=40)
    crawler.crawler()
    print("No of visited web pages: ", len(crawler.visited))
    print("No of crawled web pages: ", len(crawler.links))

    print("Comment: Uncomment the two lines of code below this comment statement in the source code to see "
          "the visited and crawled web page details.")
    #
    # pprint(crawler.visited)
    # pprint(crawler.links)
