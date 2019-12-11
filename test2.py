import requests
from bs4 import BeautifulSoup
r = requests.get('http://www.shuquge.com/txt/8072/15838947.html')
r.encoding=r.apparent_encoding
demo=r.text
soup=BeautifulSoup(demo,'html.parser')
txts=soup.find_all('div',class_="content")
soup1=soup.find_all('div',id='content')
soup2=soup.find_all('div',class_='p')
for txt1 in soup1:
    # print(txt1.text)
    txt11=txt1.text
    # print(txt11)
# print(soup1.text)
# print(soup2)
for txt3 in soup2:
    txt4=txt3.find_all('a')
    for txt5 in txt4[1:2]:
        title_1=txt5.text
for txt in txts[0:1]:
    # print(txt.h1.text)
    title = txt.h1.text
    # print(title)
    print('正在下载... '+title)
    with open(title_1+'.txt','a',encoding='utf-8') as f:
        f.write(title+'\n')
        f.write(txt11)