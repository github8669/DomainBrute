# coding=utf-8
import re

import requests
import urllib3
import json
from config import *

urllib3.disable_warnings()

def http_requests_get(url,allow_redirects=allow_redirects):
    try:
        result=requests.get(
            url=url,
            headers=headers,
            timeout=timeout,
            allow_redirects=allow_redirects,
            verify=allow_ssl_verify
        )
        return  result

    except Exception,e:

        return  requests.models.Response()


def http_request_post(url,payload,allow_redirects=allow_redirects):
    try:
        result = requests.post(
            url=url,
            data=payload,
            headers=headers,
            timeout=timeout,
            allow_redirects=allow_redirects,
            verify=allow_ssl_verify)
        return result

    except Exception,e:
        #
        return requests.models.Response()

def is_domain(domain):
    domain_regex = re.compile('[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?', re.IGNORECASE)
    return True if domain_regex.match(domain) else False


def save_result(filename,result):
    try:
        f=open(filename,'w')
        json.dump(result,f,indent=4)
    except Exception,e:
        print e


def read_json(filename):
    try:
        f=open(filename,'r')
        datas=json.load(f)
        return datas
    except Exception,e:
        print e







