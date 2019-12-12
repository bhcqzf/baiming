import requests
import parsel

# 请求网页
r = requests.get('http://www.shuquge.com/txt/63542/9645082.html')
# 编码
r.encoding = r.apparent_encoding
# 解析网站
sel = parsel.Selector(r.text)
h1 = sel.css('h1::text')
title = h1.get()
content = sel.css('#content::text')
txt = content.getall()
with open(title + 'txt', 'w', encoding='utf-8') as f:
    f.write(title)
    f.write(txt)
