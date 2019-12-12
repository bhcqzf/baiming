import requests
from bs4 import BeautifulSoup

r=requests.get('https://fdfs.xmcdn.com/group31/M0B/A9/A0/wKgJX1mubHGgS1KsAIxMu4d7ijU768.m4a')
# print(r.status_code)

with open('1'+'.mp4','wb') as fb:
    fb.write(r.content)



def downdoad_one_music():

    pass
def download_all_music():
    pass
def mian():
    pass