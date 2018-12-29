# -*- coding: utf-8 -*-
import scrapy


class IdealistaSpider(scrapy.Spider):
    name = 'idealista'
    allowed_domains = ['www.idealista.com']
    start_urls = ['http://www.idealista.com/']

    def parse(self, response):
        pass
