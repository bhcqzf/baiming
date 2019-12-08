def download_one(self):
    import requests
    from bs4 import BeautifulSoup
    r=requests.get(url)
    r.encoding=r.apparent_encoding
    demo=r.text
    # print(r.text)
    soup=BeautifulSoup(demo,'html.parser')
    # print(soup.prettify())
    title=soup.find('div',class_='bookname').h1.text
    print(title)
    txts=soup.find_all('div',id="content")
    for txt in txts:
        txt1=txt.text
        with open(title+'.txt','w',encoding='utf-8') as f:
            f.write(title)
            f.write(txt1)
'''
import requests
from lxml import etree

header={'User-Agent': 'Mozilla/5.0'}
r=requests.get('http://www.xbiquge.la/10/10489/',headers=header)
r.encoding=r.apparent_encoding
demo=r.text
# print(demo)
demo=etree.HTML(r.text)
urls=demo.xpath('//*[@id="list"]/dl/dd[1]/a')
print(urls)
# for url in urls:
# #     # download_one('http://www.xbiquge.la/10/10489/'+url)
#         print(url)
# #     # print('http://www.xbiquge.la/10/10489/'+url)
#
'''



import requests
from bs4 import BeautifulSoup
header={'User-Agent': 'Mozilla/5.0'}
r=requests.get('http://www.xbiquge.la/10/10489/',headers=header)
r.encoding=r.apparent_encoding
soup=BeautifulSoup(r.text,'html.parser')
# print(soup.prettify())
urls=soup.find_all('div',id="list")
for url1 in urls:
    url2=url1.a.get('href')
    url=('http://www.xbiquge.la/10/10489/'+url2)
    download_one(url)

#     # url1=url.get('href')