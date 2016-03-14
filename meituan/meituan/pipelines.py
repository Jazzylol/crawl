# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json


class MeituanPipeline(object):
    def __init__(self):
        self.file = codecs.open("data.txt", encoding='utf-8', mode='wb')
        self.count = 1

    # def process_item(self, item, spider):
    #     line = json.dumps(dict(item)) + '\n'
    #     self.file.write(line.decode("unicode_escape"))
    #     return item

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        value = line.decode("unicode_escape")
        self.file.write(value)
        count = self.count
        redis_client = Database()
        redis_client.write(count, value)
        self.count = count + 1
        return item


import redis


class Database:
    def __init__(self):
        self.host = 'localhost'
        self.port = 6379

    def write(self, key, val):
        try:
            r = redis.StrictRedis(host=self.host, port=self.port)
            r.set(key, val)
        except Exception, exception:
            print exception
