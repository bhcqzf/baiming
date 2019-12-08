import requests
from bs4 import BeautifulSoup
url = ('http://www.shuquge.com/txt/8072/15334945.html')
r = requests.get(url)
r.encoding=r.apparent_encoding
demo=r.text
soup=BeautifulSoup(demo,'html.parser')
title=soup.h1.text
# print(title)
txts=soup.find_all('div',id="content")
for txt in txts:
    txt1=txt.text
    with open(title+'.txt','w',encoding='utf-8') as f:
        f.write(title)
        f.write(txt1)
