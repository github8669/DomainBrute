# coding=utf-8
from utils.configs.common import http_requests_get,is_domain
import re
from requests.exceptions import RequestException

class Crt(object):
    def __init__(self,domain):
        self.domain=domain
        self.site='https://crt.sh/?q='
        self.result=[]
        self.uro=[]

    def run(self):
        url=self.site+self.domain
        try:
            r=http_requests_get(url)

            ru = re.findall('<TD>(.*?)</TD>',str(r.content))
            for i in ru :
                if str(self.domain) in i:

                    if is_domain(i):

                        self.result.append(i)

            a=list(set(self.result))
            new_websites = [w.split("<BR>") if '<BR>' in w else [w] for w in a]
            new_websites = [val for sublist in new_websites for val in sublist]
            return list(set(new_websites))

        except RequestException as e:
           print e




