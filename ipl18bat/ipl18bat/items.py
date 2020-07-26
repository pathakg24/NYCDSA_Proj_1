# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Ipl18batItem(scrapy.Item):
    player = scrapy.Field()
    bat_mat = scrapy.Field()
    bat_inns = scrapy.Field()
    bat_runs = scrapy.Field()
    bat_ave = scrapy.Field()
    bat_sr = scrapy.Field()
    
