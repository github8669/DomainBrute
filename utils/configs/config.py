# coding=utf-8

import sys
import random

#是否开启https服务器的证书校验
allow_ssl_verify=False

#线程数
thread_count=1

#超时时间
timeout=5

#是否允许url重定向
allow_redirects=True

#是否允许继承http Request类的Session支持,在发出的所有请求之间保持cookies.
allow_http_session=False

#是否允许随机的User-Agent
allow_random_useragent=False

#是否允许随机的x-Forwarded-For
allow_random_x_forward=False

#随机HTTP头
USER_AGENTS = [

    'Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5',
    'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14',

]

#随机生成User-Agent
def random_useragent(condition=False):
    if condition:
        return random.choice(USER_AGENTS)
    else:
        return USER_AGENTS[0]

#随机x-Forwarded-for,动态ip
def random_x_forward_for(condition=False):
    if condition:
        return '%d.%d.%d.%d'%(random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254))
    else:
        return '8.8.8.8'

        # HTTP头设置
headers = {
    'User-Agent': str(random_useragent(allow_random_useragent)),
    'X-FORWRDED_FOR': random_x_forward_for(allow_random_x_forward),
    'Referer': 'http://www.baidu.com',
    'Cookie': "",

}
