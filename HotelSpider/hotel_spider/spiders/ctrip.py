import scrapy


class CtripSpider(scrapy.Spider):
    name = 'ctrip'
    allowed_domains = ['ctrip.com']
    start_urls = ['http://ctrip.com/']

    def parse(self, response):
        pass
