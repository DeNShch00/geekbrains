# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from pymongo import MongoClient
from scrapy.pipelines.images import ImagesPipeline


class LeroymerlinparserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.leroymerlin_products

    def process_item(self, item, spider):
        collection = self.mongo_base[spider.name]
        collection.insert_one(item)
        return item


class LeroymerlinPhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photos']:
            for img in item['photos']:
                try:
                    yield scrapy.Request(img, cb_kwargs={'product_url': item['url']})
                except Exception as e:
                    print(e)

    def file_path(self, request, response=None, info=None):
        product_url = request.cb_kwargs['product_url']
        folder = product_url.split('/')[-2]
        file_name = request.url.split('/')[-1]
        return folder + '/' + file_name

    def item_completed(self, results, item, info):
        if results:
            item['photos'] = [x[1] for x in results if x[0]]

        return item
