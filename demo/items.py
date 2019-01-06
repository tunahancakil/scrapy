# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DemoItem(scrapy.Item):
    title = scrapy.Field()
    image_urls = scrapy.Field()
    image_name = scrapy.Field()
    image_paths = scrapy.Field()
    price = scrapy.Field()
    author = scrapy.Field()
