# coding: utf-8

from unittest import TestCase
import requests


class TestTornadoRequest(TestCase):
    base_url = "http://192.168.3.19:9000"

    def test_index_get(self):
        """测试get请求"""
        url = self.base_url + '/'

        # 查询参数
        resp = requests.get(url, params={
            'wd': 'tornado',
            # 多个相同参数名，值用列表传递
        })
        # 可能会出现400错误，原因是参数没给对
        print(resp.text)

    def test_index_post(self):
        """测试Post请求"""
        url = self.base_url + '/'
        resp = requests.post(url, data={
            'name': 'thor',
            'city': 'Mar'
        })
        print(resp.text)


class TestCookieRequest(TestCase):
    base_url = "http://192.168.3.19:9000"

    def text_cookie_delete(self):
        url = self.base_url + '/cookie'
        resp = requests.delete(url, params={
            'name': 'wd'
        })
        print(resp.txt)


class TestOrderRequest(TestCase):
    base_url = "http://192.168.3.19:9000/order"

    def test_get(self):
        resp = requests.get(self.base_url + "/1/1")
        print(resp.text)

    def test_post(self):
        resp = requests.post(self.base_url + "/1/1")
        print(resp.text)


class TestUserRequest(TestCase):
    url = "http://192.168.3.19:8000/user"

    def test_login(self):
        # 上传json数据
        resp = requests.get(self.url, json={"name": "thor", "pwd": "123"})
        # 获取响应的json数据
        print(resp.json())
