import requests
from lxml import etree
r=requests.get('https://yaohuo.me/bbs/book_list.aspx?gettotal=2020&action=new')
tree=etree.HTML(r.text)
title=tree.xpath('/html/body/div[2]/a[1]/text()')
url=tree.xpath('/html/body/div[2]/a[1]/@href')
print(title)
