# coding=utf-8
from utils.configs.common import http_requests_get
import re
from bs4 import  BeautifulSoup
from requests.exceptions import RequestException


class link(object):
    def __init__(self,domain):
        self.domain=domain
        self.site='https://www.dnsgrep.cn/subdomain/'
        self.result=[]

    def run(self):
        url=self.site+self.domain
        try:
            r=http_requests_get(url)

            resu=re.findall("<a href='/subdomain/.*?'>(.*?)</a>",str(r.content))
            htmhl=BeautifulSoup(r.text,'html.parser')

            table=htmhl.find(name="table",attrs={'data':self.domain})
            trr=table.find_all('tr')
            for tr in trr:
                td=tr.find_all(name='td',attrs={'data':re.compile(self.domain)})
                for tdd in td:
                    domintd=tdd.get('data')
                    self.result.append(domintd)
            return list(set(self.result))

        except RequestException as e:
            print e


if __name__ == '__main__':
    domain = 'ichunqiu.com'
    result = link(domain).run()
    print result
