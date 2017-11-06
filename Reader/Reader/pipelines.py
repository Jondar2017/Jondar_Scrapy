# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
import pymongo

from scrapy.conf import settings

reload(sys)
sys.setdefaultencoding('utf-8')


class ReaderPipeline(object):

    def __init__(self):
        # 获取主机名,端口,数据库
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']

        # pymongo.MongoClient(host, port),创建Mongodb链接
        client = pymongo.MongoClient(host, port)

        # 指向指定的数据库
        mdb = client[dbname]

        # 获取数据库里存放的表名
        self.post = mdb[settings['MONGODB_DOCNAME']]

    def process_item(self, item, spider):
        data = dict(item)
        # 向指定的表里添加数据
        self.post.insert(data)
        return item
