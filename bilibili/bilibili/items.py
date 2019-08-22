# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    '''
    名字，观看次数，图片地址
    '''
    title = scrapy.Field()
    watch = scrapy.Field()
    image = scrapy.Field()

