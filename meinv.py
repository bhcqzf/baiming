import requests
import re

# 请求网页
header = {'User-Agent': 'Mozilla/5.0'}
r = requests.get('https://www.vmgirls.com/9384.html', headers=header)
r.encoding = r.apparent_encoding
# print(r.request.headers)

html = r.text
# print(html)
# 解析网站
urls = re.findall(
    '<img alt=".*?" src=".*?" width="2904" height="4356" class="alignnone size-full" data-src="(.*?)" data-nclazyload="true">',
    html)
# print(urls)

for url in urls:
    response = requests.get(url, headers=header)
    file_name = url.split('/')[-1]
    with open(file_name, 'wb') as f:
        f.write(response.content)
