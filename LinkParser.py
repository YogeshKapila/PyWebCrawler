"""
1. Parse a given link and extract new links
2. Add links to a repository
3. Move to the next link in repository
4. Stop after a max limit of links has been opened
"""
from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse
from pprint import pprint

from UrlProcessor import UrlProcessor


class LinkParser(HTMLParser):
    def __init__(self, seed_url):
        """
        Initialize the Link Parser
        :param seed_url: The Seed Url for the Crawler
        """
        self.url_processor = UrlProcessor()
        if self.url_processor.check_if_valid_url(seed_url):
            self.seed = seed_url
        else:
            print ("Invalid Seed URL: {}".format(seed_url))

        # Unique set of links on the page
        self.links = set()
        super().__init__()

    def handle_starttag(self, tag, attrs):
        """
        Override base class method.
        """
        # Detect links like <a href="www.exampleurl.com"></a>
        if tag == 'a':
            # pprint(attrs)
            for (key, value) in attrs:
                if key == 'href':
                    newUrl = parse.urljoin(self.seed, value)
                    self.links.add(newUrl)
                    # print(len(self.links), self.links)

    def get_all_links(self):
        """
        Get all links on the self.seed url page.
        :return: None
        """
        try:
            response = urlopen(self.seed)
            content_type = response.getheader('Content-Type')
            # print(content_type)
            if 'text/html' in content_type:
                raw_resp = response.read()
                # print(type(raw_resp), raw_resp)

                # Decode byte Stream
                str_resp = raw_resp.decode("utf-8")
                self.feed(str_resp)
        except Exception as error:
            # Skip Error and continue
            print(error)


class TestLinkParser:
    def __init__(self, seed_url):
        self.link_parser = LinkParser(seed_url)


if __name__=="__main__":
    response = urlopen("http://www.pythonforbeginners.com/super/working-python-super-function")
    htmlbytes = response.read()
    htmlstr = htmlbytes.decode("utf-8")
    parser = LinkParser(seed_url="http://www.pythonforbeginners.com/super/working-python-super-function")

    parser.feed(htmlstr)
    parser.get_all_links()
