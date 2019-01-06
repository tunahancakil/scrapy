# -*- coding: utf-8 -*-
import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'ide'
    start_urls = [
        'https://www.idefix.com/CokSatanlar/Kitap',
    ]

    def parse(self, response):
        for quote in response.xpath('//div[@class="columnContent"]'):
            yield {
                'text': quote.xpath('./a[@class="newPrice"]/text()').extract_first(),
                'author': quote.xpath('.//small[@class="author"]/text()').extract_first(),
                'tags': quote.xpath('.//h3[@class="productName bold"]/text()').extract()
            }

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))


