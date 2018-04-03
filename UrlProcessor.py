"""
Process a URL for
1. Validity
2. Extraction of Base URL
3. Others
"""

import validators


class UrlProcessor:
    def __init__(self):
        pass

    @classmethod
    def check_if_valid_url(cls, url):
        # print("Checking {}".format(url))
        result = validators.url(url)
        if type(result) == validators.utils.ValidationFailure:
            print("Invalid URL..")
            return False
        print("Valid URL..")
        return True


class TestUrlProcessor:
    def __init__(self):
        self.url_procesor = UrlProcessor()

    def test_url_validator(self):
        url_1 = "http://google"
        url_2 = "http://google.com"
        url_3 = "google"
        url_4 = "google.com"
        assert not self.url_procesor.check_if_valid_url(url_1), "Test URL Failed for URL: {}".format(url_1)
        assert self.url_procesor.check_if_valid_url(url_2), "Test URL Failed for URL: {}".format(url_2)
        assert not self.url_procesor.check_if_valid_url(url_3), "Test URL Failed for URL: {}".format(url_3)
        assert not self.url_procesor.check_if_valid_url(url_4), "Test URL Failed for URL: {}".format(url_4)


if __name__=="__main__":
    tester = TestUrlProcessor()
    tester.test_url_validator()