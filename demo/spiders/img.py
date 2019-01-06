import scrapy 

class PexelsScraper(scrapy.Spider): 
    name = "pexels"
    def start_requests(self): 
        url = "https://www.pexels.com/" 
        yield scrapy.Request(url, self.parse) 
    
    def parse(self, response):
        print (response.url, response.body)


