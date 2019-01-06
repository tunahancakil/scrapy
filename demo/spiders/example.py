import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from demo.items import DemoItem

class DemoSpider(CrawlSpider):
    name = 'N11'
    allowed_domain = ['www.n11.com']
    start_url = ['https://www.n11.com']

    rules = [Rule(LinkExtractor(allow=['/kitap']), 'parse_n11')]

    def parse_imgur(self, response):
        image = DemoItem()
        image['title'] = response.xpath("//h3[@class='productName bold']/text()").extract()
        rel = response.xpath("//img[@class='lazy']/@src").extract()
        image['image_urls'] = ['http:'+rel[0]]
        return image
