# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
import logging
import re


class DemoPipeline(ImagesPipeline):
 
    CONVERTED_ORIGINAL = re.compile('^full/[0-9,a-f]+.jpg$')
    
    '''def get_media_requests(self, item, info):
        for urls in item['image_urls']:
            for url in urls:
                yield scrapy.Request(url,meta={'title': item['title']})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]           
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item  ''' 


    def get_media_requests(self, item, info):
        print ("get_media_requests")
        for x in item.get('image_urls', []):
            print(x)
        return [scrapy.Request(x, meta={'image_names': item["image_name"]})
                for x in item.get('image_urls', [])]

    # this is where the image is extracted from the HTTP response
    def get_images(self, response, request, info):
        print ("get_images")
        for key, image, buf, in super(DemoPipeline, self).get_images(response, request, info):
            print(response)
            if self.CONVERTED_ORIGINAL.match(key):
                key = self.change_filename(key, response)
            yield key, image, buf

    def change_filename(self, key, response):
        return "full/%s.jpg" % response.meta['image_names'][i]         

    '''def get_images(self, response, request, info):
        for key, image, buf in super(DemoPipeline, self).get_images(response,request,info):
            key = self.set_filename(response)
            yield key, image, buf
    '''
        