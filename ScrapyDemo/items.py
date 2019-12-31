# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapydemoItem(scrapy.Item):
    # song name
    song_name = scrapy.Field()
    # song lyrics
    song_lyrics = scrapy.Field()
