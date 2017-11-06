# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ReaderItem(scrapy.Item):
    # 文章期刊
    magazine = scrapy.Field()
    # 文章题目
    title = scrapy.Field()
    # 作者
    writer = scrapy.Field()
    # 每一篇文章的链接
    link = scrapy.Field()
    # 文章内容
    contents = scrapy.Field()
