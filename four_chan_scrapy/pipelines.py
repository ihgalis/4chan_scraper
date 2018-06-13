# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class MongoPipeline(object):
    collection_name = 'four_chan'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        """
        Check whether the element has already been added to the database

        :param item:
        :param spider:
        :return:
        """
        # get current hash
        dict_item = dict(item)
        current_hash = dict_item['identityhash']

        # find it in db
        result = self.db[self.collection_name].find_one({'identityhash': current_hash})

        # if there is no result the item is new
        if result is None:
            self.db[self.collection_name].insert_one(dict(item))
            return item
        # otherwise there is nothing to do
        else:
            return item
