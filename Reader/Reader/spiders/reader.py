# -*- coding: utf-8 -*-
import scrapy
import json

from Reader.items import ReaderItem


class ReaderSpider(scrapy.Spider):
    name = "reader"
    allowed_domains = ["52duzhe.com"]
    offset = 1
    url = "http://www.52duzhe.com/2017_0"
    start_urls = (url + str(offset) + "/index.html", )

    def parse(self, response):
        base_index = response.xpath('//div[@class="blkContainer"]')
        item = ReaderItem()
        # 获取期刊
        magazine = base_index.xpath('.//h1/text()').extract()[0]
        item['magazine'] = magazine[:-2]
        # print item['magazine']
        # 获取每一篇文章的url
        links = base_index.xpath('.//tr/td[@class="title"]/a/@href').extract()
        for link in links:
            # 组合新的url地址
            link = "http://www.52duzhe.com/2017_0" + str(self.offset) + '/' + link
            item['link'] = link
            # print link
            yield scrapy.Request(link, meta={'meta': item}, callback=self.parse_item)

        if self.offset < 6:
            self.offset += 1
            yield scrapy.Request(self.url + str(self.offset) + '/index.html', callback=self.parse)

    def parse_item(self, response):
        meta = response.meta['meta']
        contents = ''
        art_index = response.xpath('//div[@class="blkContainer"]')
        # 获取文章标题
        meta['title'] = art_index.xpath('.//h1/text()').extract()[0]
        # 获取作者
        meta['writer'] = art_index.xpath('.//div[@class="artInfo"]/span[@id="pub_date"]/text()').extract()[0].strip()
        # 获取文章内容
        content_list = art_index.xpath('.//p/text()').extract()

        for content_one in content_list:
            contents += content_one + '\n'

        meta['contents'] = contents

        yield meta


