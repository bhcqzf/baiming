# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class BiquPipeline(object):
    def __init__(self):
        self.f=open('./三寸人间.txt','a',encoding='utf-8')
    def process_item(self, item, spider):
        self.f.write(item['title']+'\n')
        for p in item['content']:
            self.f.write(p)
        else:
            self.f.write('\n')
        return item
    def close_spider(self,spider):
        self.f.close()
