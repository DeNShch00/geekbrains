# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UserItem(scrapy.Item):
    _id = scrapy.Field()
    user_id = scrapy.Field()
    name = scrapy.Field()
    full_name = scrapy.Field()
    pic_url = scrapy.Field()


class UserFollowItem(scrapy.Item):
    _id = scrapy.Field()
    user_id = scrapy.Field()
    follow_id = scrapy.Field()
    follow_type = scrapy.Field()
