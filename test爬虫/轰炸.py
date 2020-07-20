import requests
import time
from chaojiying import Chaojiying_Client
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
def get_code():
    time_stamp = str(int(time.time() *1000))
    # print(time_stamp)
    url = 'https://creditcard.ecitic.com/citiccard/ucweb/newvalicode.do?time='+time_stamp
    res=requests.get(url,headers=headers)
    cookies = res.cookies
    cookies = cookies.get_dict()
    with open('yzm.jpeg','wb') as f:
        f.write(res.content)
    return cookies
def send_sms(cookies):
    time_stamp = str(int(time.time() *1000))
    chaoji=Chaojiying_Client('bhcqzf','.zZ.qVn5tdG.27D','906614')
    im = open('yzm.jpeg', 'rb').read()
    code=chaoji.PostPic(im, 1004)
    print(code)
    url2 = 'https://creditcard.ecitic.com/citiccard/ucweb/getsms.do?&timestamp'+time_stamp
    data={'phone': '15102517719',
         'imgValidCode':code['pic_str']}
    res2=requests.post(url2,cookies=cookies,headers=headers,data=data)
    print(res2.text)
def main():
    cookies=get_code()
    send_sms(cookies)
if __name__ == '__main__':
    main()