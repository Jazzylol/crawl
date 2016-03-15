# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

import utils.RedisHelper
import utils.MongoHelper


class MeituanPipeline(object):
    def __init__(self):
        self.file = codecs.open("data.txt", encoding='utf-8', mode='wb')
        self.count = 1

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        value = line.decode("unicode_escape")
        try:
            self.file.write(value)
        except Exception, e:
            print e
        finally:
            self.file.close()
        try:
            count = self.count
            redis_helper = utils.RedisHelper.RedisHelper()
            redis_helper.set_obj(count, value)
            self.count = count + 1
        except Exception, e:
            print e
        try:
            mongo_client = utils.MongoHelper.MongoHelper()
            mongo_client.insert(value)
        except Exception, e:
            print e
        return item
