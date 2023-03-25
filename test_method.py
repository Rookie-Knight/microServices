# coding: utf-8

from unittest import TestCase
import requests


class TestTornadoRequest(TestCase):
    base_url = "http://192.168.3.19:9000"

    def test_index_post(self):
        url = self.base_url + '/'
        resp = requests.post(url, data={
            'name': 'thor',
            'city': 'Mar'
        })
        print(resp.text)



