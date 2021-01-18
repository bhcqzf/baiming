# -*- coding: utf-8 -*-
import scrapy
from ITcast.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['http://www.itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # print(response.body.decode('utf-8'))
        node_list=response.xpath('//*[@class ="main_mask"]')
        # items=[]
        for node in node_list:
            # 创建一个item对象
            item = ItcastItem()
            name=node.xpath('./h2/text()').extract()
            title=node.xpath('./h2/span/text()').extract()
            info=node.xpath('./p/text()').extract()
            item['name']=name[0]
            item['title'] = title[0]
            item['info']=info[0].strip()
            yield item
            # items.append(item)
        # return items
        # # 姓名
        # //*[@class ="main_mask"]/h2/text()
        # #职称
        # //*[@class="main_mask"]/h2/span/text()
        # # 简介
        # //*[@class="main_mask"]/p/text()
        # pass
