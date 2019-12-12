import requests
from bs4 import BeautifulSoup
def download_one_charcter(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    demo = r.text
    soup = BeautifulSoup(demo, 'html.parser')                   #这里写了好几遍，半夜写的，思路很乱，写的很麻烦，有时间改一改
    txts = soup.find_all('div', class_="content")
    soup1 = soup.find_all('div', id='content')
    soup2 = soup.find_all('div', class_='p')
    for txt1 in soup1:
        # print(txt1.text)
        txt11 = txt1.text
        # print(txt11)
    # print(soup1.text)
    # print(soup2)
    for txt3 in soup2:
        txt4 = txt3.find_all('a')
        for txt5 in txt4[1:2]:
            title_1 = txt5.text
    for txt in txts[0:1]:
        # print(txt.h1.text)
        title = txt.h1.text
        # print(title)
        print('正在下载... ' + title)
        with open(title_1 + '.txt', 'a', encoding='utf-8') as f:
            f.write(title + '\n')
            f.write(txt11)
    pass
bookmulu='http://www.shuquge.com/txt/8072/index.html'   #此处为要下载小说的目录链接
r=requests.get(bookmulu)
bookmulu_pre=bookmulu.replace('index.html','')
r.encoding=r.apparent_encoding
demo=r.text
soup=BeautifulSoup(demo,'html.parser')
one_titles=soup.find_all("div",class_="listmain")
# print(one_titles)
for item in one_titles:
    txts=item.find_all('a')
    # print(item)
    # print(txts)
    for tag_a in txts[12:]:
        # print(tag_a)
        one_url=tag_a.get('href')
        # print(one_url)
        # one_title=tag_a.text
        # print(one_title)
        url=(bookmulu_pre+one_url)
        # print(url)
        download_one_charcter(url)

