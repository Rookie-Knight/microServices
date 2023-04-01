# -*- coding: utf-8 -*-
import os

from tornado.web import RequestHandler
from tornado.httpclient import HTTPClient, HTTPResponse, HTTPRequest


class DownloadHandeler(RequestHandler):
    def get(self):
        # 获取查询参数中的url(下载资源的网址)
        url = self.get_query_argument('url')
        file_name = self.get_query_argument('filename','index.html')

        # 发起同步请求
        client = HTTPClient()
        # validate_cert 是否验证SSL安全链接的证书
        response: HTTPResponse = client.fetch(url, validate_cert=False)
        # 保存到/static/dowloads下
        with open(os.path.join("./static/downloads/", file_name), 'wb') as f:
            f.write(response.body)
            self.write("下载成功!")