#-*- coding:utf-8 -*-

import requests
import time
import datetime
import threading
import json
import sys


# 设置为微信内置浏览器模式 加个micromessenger字符串
ua_list = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0 micromessenger"


class CustomTask:
    def __init__(self):
        self._result = None

    def run(self, url, data, code=0):
        my_headers = {
            'Content-Type': 'application/json;charset=utf-8',
            'Host': 'u9hb4f.fanqier.com',
            'Origin': 'https://u9hb4f.fanqier.comm',
            # 'Referer': 'https://uu11lpc.fanqier.com/f/yqgfzf',
            'User-Agent': ua_list,
        }
        try:
            result = requests.post(url=url, data=json.dumps(data), headers=my_headers)
        except requests.exceptions.ConnectionError:
            print "连接失败"
        else:
            date = datetime.datetime.now().strftime('%H:%M:%S')
            print u"第%s次 [%s] 状态：%s " % (code + 1, date, result.text)
            result1 = result.json()['status']['message']
            self._result = result1

    def get_result(self):
        return self._result

def set_data():
    # 需要修改definition的值
    obj = {"definition": "58f42de0c4ea760fbc90570c", "type": "title"}
    # 设置姓名，需要修改definition和value的值
    name = {"definition": "58f42eedb3e56486ea000002", "type": "text", "value": "张三", "isNumber": "false"}
    # 设置学号，需要修改definition和value的值
    card = {"definition": "58f42eeeb3e56486ea000003", "type": "text", "value": "*******", "isNumber": "true"}
    # 设置电话号码，需要修改definition和value的值
    phone = {"definition": "593df9dac442a7291a000005", "type": "text", "value": "******", "isNumber": "true"}
    # 设置请求的url，修改最后的一长串数字
    url = 'https://u9hb4f.fanqier.com/api/f/59c9b5c95fa7264dea1f55b4'
    # 需要修改formId的值
    data = {"values": [obj, name, card, phone],
             "formId": "59c9b5c95fa7264dea1f55b4",
             "wechat": "1234",
             "duration": 73673
             }
    main(url, data)


def main(url, data):
    print '----------start--------------'
    for i in range(6000):
         #启动线程，每隔1s产生一个线程，可通过控制时间加快投票速度
         ct = CustomTask()
         t1 = threading.Thread(target=ct.run, args=(url, data, i))
         t1.start()
         time.sleep(1)  # time.sleep的最小单位是毫秒，当前设置的是1秒
         result = ct.get_result()
         if result == "success":
             print u"抢票成功，即将退出程序。。。"
             sys.exit()


if __name__ == '__main__':
    print u'前沿讲座抢票小程序:输入1开始抢票，输入2退出程序'
    number = int(raw_input("please input number,and press enter:"))
    if number == 1:
        set_data()
    elif number == 2:
        sys.exit()
