import requests
from bs4 import BeautifulSoup
import re



'''下载一章'''
def downdoad_one_music(one_book_title,one_page_url,one_title):
    ture_api = ('https://www.ximalaya.com/revision/play/v1/audio?id=' + one_page_url + '&ptype=1')
    header = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(ture_api, headers=header)
    demo = r.text
    # print(r.status_code)
    r.encoding = r.apparent_encoding
    # print(r.text)
    soup = BeautifulSoup(demo, 'lxml')
    # print(soup.prettify())
    url_ids = soup.p.text
    # print(url_ids)
    final_url = re.findall('"src":"(.*?)"', url_ids)[0]
    # print(final_url)



    r = requests.get(final_url)
    # print(r.status_code)

    with open('有声书'+'/'+one_title + '.mp4', 'wb') as fb:
        print('正在下载。。。' + one_title)
        fb.write(r.content)


    pass
'''获取所有小说的id'''
def get_all_pages(url_first):               #此处输入小说目录首页
    header = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url_first, headers=header)
    r.encoding = r.apparent_encoding
    demo = r.text
    # print(r.status_code)

    # print(r.text)
    soup = BeautifulSoup(demo, 'lxml')
    # print(soup.prettify())
    url_ids = soup.select('#anchor_sound_list > div.sound-list._c2 > div > nav > ul > li:nth-child(7) > a > span')
    n = url_ids[-1].text
    n = int(n)
    # print(n)
    for i in range(n):
        i = str(i)
        one_page = ('https://www.ximalaya.com/youshengshu/10331475/p' + i)
        # print(one_page)
        header = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(one_page, headers=header)
        demo = r.text
        # print(r.status_code)
        r.encoding = r.apparent_encoding
        # print(r.text)
        soup = BeautifulSoup(demo, 'lxml')
        # print(soup.prettify())
        url_ids = soup.select('#anchor_sound_list > div.sound-list._c2 > ul > li> div.text._c2 > a')
        one_book_title = soup.select(
            '#award > main > div.album-detail > div.clearfix > div.detail.layout-main > div.detail-wrapper._II0L > div.album-info.clearfix._II0L > div.info._II0L > h1')[
            0].text
        # print(one_book_title)
        # print(url_ids)
        for url_id in url_ids:
            # print(url_id.attrs)
            one_page_url = url_id.get('href').split('/')[-1]
            one_title = url_id.get('title')
            # print(one_title)
            # print(one_page_url)
            downdoad_one_music(one_book_title,one_page_url, one_title)

    pass
# def main():
# url_first='https://www.ximalaya.com/youshengshu/10331475/'
get_all_pages('https://www.ximalaya.com/youshengshu/10331475/')   #此处输入小说主页
    # pass
# if __name__=='__main__':
#     main()
