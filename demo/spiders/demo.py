import scrapy
from demo.items import DemoItem

class MySpider(scrapy.Spider):
    name = 'example.com'
    allowed_domains = ['example.com']

    def start_requests(self):
        yield scrapy.Request('https://www.hepsiburada.com/kitaplar-c-2147483645', self.parse)
       
    def parse(self, response):
        for h3 in response.xpath('//h3').extract():
            yield DemoItem(title=h3)

        for url in response.xpath('//a/@href').extract():
            yield scrapy.Request(url, callback=self.parse)