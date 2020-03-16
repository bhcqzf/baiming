import requests
import json
import random
api="101070101"
r = requests.get('http://t.weather.sojson.com/api/weather/city/'+api)
r.encoding = r.apparent_encoding
a = r.text
data=json.loads(a)
city=data["cityInfo"]["city"]
shi=data["cityInfo"]["parent"]
date=data['time']
forecastdata=data["data"]["forecast"][0]
quality=data["data"]["quality"]
high=forecastdata["high"]
low=forecastdata["low"]
week=forecastdata["week"]
typea=forecastdata["type"]
fx=forecastdata["fx"]
fl=forecastdata["fl"]
ra=random.randint(0,14)
最后一句=["您的亲爹真诚的提醒您，今天也要援气满满哦！",
      "卧槽，二狗你干啥呢",
      "爹要去睡了，拜拜",
      "每天起床第一句：你平胸，你骄傲，你为国家省布料",
      "可爱既是正义，大胸才有底气",
      "我可以摸摸你的胸么",
      "渣男锡纸烫，渣女大波浪",
      "中国人口那么多，而我却没有人口",
      "但愿人长久，此事古难全",
      "这周日你有空么？",
      "喜欢上一个人",
      "比起一见钟情，我更喜欢日久生情",
      "因为喜欢上你，所以才明白什么叫做爱",
      "即使爹不在身边，你也要努力欢笑",
      "弱水三千，我只嫖你一个"]
print("早上好，我是你爹啊~~")
print("爹猜你肯定没看天气预报")
print("所以现在爹给你播报天气")
print("你现在处在的位置是：憋屈的"+shi+city)
print("现在时间为："+date+" "+week)
print("今天的天气是："+typea+" "+fx+fl+" "+high+" "+low+" 天气指数："+quality)
print(最后一句[ra])
