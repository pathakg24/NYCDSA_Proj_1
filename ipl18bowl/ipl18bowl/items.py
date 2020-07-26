# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Ipl18bowlItem(scrapy.Item):
    player = scrapy.Field()
    bowl_mat = scrapy.Field()
    bowl_inns = scrapy.Field()
    wkts = scrapy.Field()
    econ = scrapy.Field()
    bowl_sr = scrapy.Field()
    catches = scrapy.Field()
