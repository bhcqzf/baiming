import requests
import json
api="101090506"
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
print("早上好，我是你爹啊~~")
print("爹猜你肯定没看天气预报")
print("所以现在爹给你播报天气")
print("你现在处在的位置是：憋屈的"+shi+city)
print("现在时间为："+date+" "+week)
print("今天的天气是："+typea+" "+fx+fl+" "+high+" "+low+" 天气指数："+quality)
print("您的亲爹真诚的提醒您，今天也要元气满满哦！")

