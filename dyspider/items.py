# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    uid = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    section = scrapy.Field()
    category = scrapy.Field()
    pubdate = scrapy.Field()
