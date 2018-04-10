import scrapy
from scrapy_splash import SplashRequest


class SplashSpider(scrapy.Spider):
    name = 'scrapy_splash'
    start_urls = ["http://example.com", "http://example.com/foo"]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        print (response.body)
        # response.body is a result of render.html call; it
        # contains HTML processed by a browser.
        # ...