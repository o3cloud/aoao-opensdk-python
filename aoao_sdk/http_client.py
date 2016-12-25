# _*_ coding: utf-8 _*_
import requests
from . import aoao_url


class RequestsClient(object):
    """构造嗷嗷请求"""
    @staticmethod
    def request(data, method='post', url=aoao_url):
        headers = {
            "Content-Type": "multipart/form-data"
        }
        try:
            r = requests.request(method, url, data=data, headers=headers)
        except requests.ConnectionError:
            return
        return r
