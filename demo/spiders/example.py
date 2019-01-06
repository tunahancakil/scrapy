import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from demo.items import DemoItem
import logging

class DemoSpider(CrawlSpider):
    name = 'N11'
    allowed_domain = ['www.n11.com']
    start_url = ['https://www.n11.com']

    

    rules = [Rule(LinkExtractor(allow=['/kitap']), 'parse_n11')]

    def start_requests(self):
        urls = ['https://www.idefix.com/kategori/Kitap/Edebiyat/grupno=00055']
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_imgur)

    def parse_imgur(self, response):
        image = DemoItem()
        image['title'] = response.xpath("//div[@class='image-area']//img/@alt").extract()  
        rel = []
        for node in response.xpath("//div[@class='row']"):              
                rel.append(node.xpath("//div[@class='image-area']//img/@src").extract())
                image['image_name'] = response.xpath("//div[@class='image-area']//img/@alt").extract()
                image['price'] = node.xpath("//span[@class='price price']/text()").extract()
                image['author'] = node.xpath("//a[@class='who']/text()").extract()

        image['image_urls'] = rel[0]
        
        logging.info(image)
        return image
