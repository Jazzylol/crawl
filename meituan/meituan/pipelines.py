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

    # def process_item(self, item, spider):
    #     line = json.dumps(dict(item)) + '\n'
    #     self.file.write(line.decode("unicode_escape"))
    #     return item

    def process_item(self, item, spider):
        divstr = eval(eval(str(item))['divstr'])['data'].decode("unicode_escape").replace("\/","/")
        print(divstr)
        return item
