# -*- coding: utf-8 -*-
import scrapy
import re

class worddef(scrapy.Item):
    word = scrapy.Field()
    defi = scrapy.Field()

class AlphaSpider(scrapy.Spider):
    name = 'alpha'
    allowed_domains = ['dictionary.com']

    def __init__(self, words):
        self.start_urls = ["http://dictionary.com/browse/" + w for w in words.split(",")]
        print(self.start_urls)

    def parse(self, response):
        item = worddef()
        item["word"] = response.css("h1::text").get()
        item["defi"] = response.css("div.e16867sm0:first-of-type span.e1q3nk1v4::text").getall()
        yield item
