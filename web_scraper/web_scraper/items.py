# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field
from scrapy.loader.processors import TakeFirst, Join, Compose
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule



class Location(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    year = Field()
    hostCity = Field()
    hostCountry = Field()
    numAthletes = Field()
    numCountries = Field()
    numEvents = Field()
    date = Field()

#     rules = (
#     Rule(
#         LinkExtractor(
#             allow=r'\d+/\d+/\d+/.+/',
#             process_value=self.process_value
#         ),
#         callback='parse_item'
#     ),
# )
    pass
