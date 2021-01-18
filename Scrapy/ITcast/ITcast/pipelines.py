# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
class ItcastPipeline(object):
    def __init__(self):
        self.f=open('./itcast.json','wb')
        # pass
    def process_item(self, item, spider):
        content=json.dumps(dict(item),ensure_ascii=False)
        self.f.write(content.encode('utf-8'))
        return item
    def close_spider(self,spider):
        self.f.close()
        # pass