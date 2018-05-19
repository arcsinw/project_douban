# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
 
class Movie(scrapy.Item):
    title = scrapy.Field()
    src = scrapy.Field()
    index = scrapy.Field()
    star = scrapy.Field()
    info = scrapy.Field()
