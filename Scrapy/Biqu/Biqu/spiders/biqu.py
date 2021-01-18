# -*- coding: utf-8 -*-
import scrapy
from Biqu.items import BiquItem

class BiquSpider(scrapy.Spider):
    name = 'biqu'
    allowed_domains = ['www.xbiquge.la']
    start_urls = ['http://www.xbiquge.la/10/10489/4535761.html']

    def parse(self, response):
        item=BiquItem()
        title = response.xpath('//h1/text()').extract()
        content = response.xpath('//*[@id="content"]/text()').extract()
        next_page = response.xpath('//div[@class="bottem1"]/a[4]/@href').extract()[0]
        next_url = 'http://www.xbiquge.la'+ next_page
        # print(title[0])
        # print(content)
        item['title']=title[0]
        item['content']=content
        # print(type(item['content']))
        # print(title)
        # print(next_page)
        yield item
        if next_page != '/10/10489/':
            yield scrapy.Request(next_url,callback=self.parse)