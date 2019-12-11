from bs4 import BeautifulSoup
import requests
r = requests.get('http://www.shuquge.com/txt/8072/')
r.encoding = r.apparent_encoding
demo = r.text
soup=BeautifulSoup(demo,'lxml')
txts = soup.find('div', class_="listmain").dl.descendants
# child1=txts.conents.dd
for child in txts:

    print(child.a)    #待修改