import json
import datetime
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
import requests
from collections import OrderedDict
from Crypto.PublicKey import RSA
import base64
import re


from getToken import getToken
import argparse
import show
from getWeek import getWeek

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--username', help='username',default=202107024000)#你的学号
parser.add_argument('-p', '--password', help='password',default=8888)#身份证后六位
parser.add_argument('-s', '--starttime', help='starttime',default=9.5)#起始时间 
parser.add_argument('-e', '--endtime', help='endtime',default=21)#结束时间
parser.add_argument('-seat', '--seat', help='seat',default='1687')#座位id，可以到浏览器抓包查看seatId，例如1687为三南61号
args = parser.parse_args()
username=args.username
password=args.password
token=getToken(username,password)
date=(datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d")
weekday=getWeek()
starttime=9.5
endtime=21
if weekday==1:
    starttime=14.5
args=parser.parse_args()
# seat='1804'
seat=args.seat
starttime1=str(int(starttime*60.0))
endtime1=str(int(endtime*60.0))
print(token)


def work():
    url = 'https://seat.ncist.edu.cn/rest/v2/freeBook?token='+token
    requests.packages.urllib3.disable_warnings()
    header = {
        "Host":"seat.ncist.edu.cn",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:124.0) Gecko/20100101 Firefox/124.0",
        "Accept": "application/json, text/plain, */* ",
         "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
         "Accept-Encoding": "gzip, deflate",
         "loginType":"PC",
         "Authorization": token,
         "Content-Type": "multipart/form-data; boundary=---------------------------99985450640619535411967254881",
         "Content-Length": "888",
         "Origin":"https://seat.ncist.edu.cn",
         "Connection": "close",
         "Referer": "https://seat.ncist.edu.cn/libseat/",
         "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "token":token
    }

    datas = OrderedDict([("startTime", (None, starttime1,)),
                          ("endTime", (None, endtime1,)),
                          ('seat', (None, seat,)),
                          ('date', (None, date,)),
                          ('userId', (None, '19196',)),
                          ('username', (None, username,)),
                          ('authid', (None, '',)),])

    res =requests.post(url,headers=header,files=datas,verify=False)
    a=res.request.body
    a=a.decode("utf-8")
    temp = re.search(r'--(.*)--',a).group(1)
    data = re.sub(temp, '---------------------------99985450640619535411967254881',a)
    res = requests.post(url, headers=header, data=data, verify=False)
    print(res.text)
    if 'success' in res.text:
        show.show_success()
    else:
        show.show_fail()


if __name__ == '__main__':
    work()