# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapisosItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    rooms = scrapy.Field()
    m2 = scrapy.Field()
    planta = scrapy.Field()
    ascensor = scrapy.Field()
    comentarios = scrapy.Field()

class SellItem(IdealistaItem):
    drop_price = scrapy.Field()
    price_per_m2 = scrapy.Field()

class RentItem(IdealistaItem):
    rent = scrapy.Field()
