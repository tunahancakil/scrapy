# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DemoItem(scrapy.Item):
    title = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()

class ImagecrawlItem(scrapy.Item):
    host= scrapy.Field()
    s=scrapy.Field()
    src_link = scrapy.Field()