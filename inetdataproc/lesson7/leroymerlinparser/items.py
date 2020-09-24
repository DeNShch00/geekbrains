# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst


def price_to_int(price: str):
    if price:
        return int(price.replace(' ', ''))

    return price


def format_props_value(value: str):
    if value:
        return value.strip()

    return value


class LeroymerlinparserItem(scrapy.Item):
    name = scrapy.Field(output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(price_to_int), output_processor=TakeFirst())
    photos = scrapy.Field()
    props_names = scrapy.Field()
    props_values = scrapy.Field(input_processor=MapCompose(format_props_value))
    props = scrapy.Field()
    _id = scrapy.Field()
