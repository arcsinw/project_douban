# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from project_douban.items import Movie

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']
    
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en',
        'User-Agent' : 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36',
    }

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS' : headers,
        'REDIRECT_ENABLED' : 'False',
        'LOG_LEVEL' : 'WARNING',

    }

    def parse(self, response):
        items = response.xpath('//div[@class="item"]')

        for item in items:
            movie = Movie()
            movie['index'] = item.xpath('div//em/text()')[0].extract()
            self.logger.info(movie['index'])

            movie['src'] = item.xpath('div//img/@src')[0].extract()
            self.logger.info(movie['src'])

            movie['title'] = item.xpath('.//div[@class="hd"]/a/span[1]/text()').extract()[0] #.xpath('string(.)').extract()).replace(' ','').replace('\xa0',' ').replace('\n',' ')
            self.logger.info(movie['title'])

            movie['star'] = item.xpath('.//span[@class="rating_num"]/text()').extract()[0]
            self.logger.info(movie['star'])
            
            movie['info'] = item.xpath('.//div[@class="bd"]/p').xpath('string(.)')[0].extract().strip().replace(' ','').replace('\xa0',' ').replace('\n',' ')
            self.logger.info(movie['info'])

            yield movie
        
        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield Request(next_url, headers = self.headers)

