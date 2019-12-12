import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.xbiquge.la/0/951/827335.html')
r.encoding = r.apparent_encoding
demo = r.text
# print(r.text)
soup = BeautifulSoup(demo, 'lxml')
# print(soup.prettify())
booktitle = soup.select('#wrapper > div.content_read > div > div.con_top > a')[-1].text
print(booktitle)
title = soup.find('div', class_='bookname').h1.text
print(title)
txts = soup.find_all('div', id="content")
for txt in txts:
    txt1 = txt.text
    with open(booktitle + '.txt', 'a', encoding='utf-8') as f:
        print(txt1)
        f.write(title + '\n')
        f.write(txt1 + '\n' + '\n')
