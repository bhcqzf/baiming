import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.bilibili.com/')
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
print(soup.prettify())
