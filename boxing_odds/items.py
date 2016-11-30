# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BoxingOddsItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    link = scrapy.Field()
    time = scrapy.Field()
    date = scrapy.Field()
    result = scrapy.Field()
    fight = scrapy.Field()
    win1 = scrapy.Field()
    draw = scrapy.Field()
    win2 = scrapy.Field()
    bookmakers = scrapy.Field()
    pass
