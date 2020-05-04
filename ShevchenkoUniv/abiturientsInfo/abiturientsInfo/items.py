# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class Abiturient(Item):
    name = Field()
    mark = Field()
    priority = Field()
    status = Field()
    docs = Field()
    faculty = Field()
    specialty = Field()
