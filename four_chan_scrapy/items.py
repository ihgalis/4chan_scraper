# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FourChanScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    board = scrapy.Field()
    datetime = scrapy.Field()
    posttext = scrapy.Field()
    identityhash = scrapy.Field()
    postnum = scrapy.Field()


class FourChanImageItem(scrapy.Item):
    postnum = scrapy.Field()
    image_url = scrapy.Field()
