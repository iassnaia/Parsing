# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScraperHw6Item(scrapy.Item):
    book_name = scrapy.Field()
    book_price = scrapy.Field()
    book_available = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
