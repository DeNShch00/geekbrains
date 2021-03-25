# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from instagramparser.items import UserItem, UserFollowItem
from pymongo import MongoClient


class InstagramparserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.instagram_users

    def process_item(self, item, spider):
        if isinstance(item, UserItem):
            collection = self.mongo_base['users']
            collection.update_one({'user_id': item['user_id']}, {'$set': item}, upsert=True)
        elif isinstance(item, UserFollowItem):
            collection = self.mongo_base['follow']
            collection.insert_one(item)

        return item
