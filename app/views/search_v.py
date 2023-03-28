# -*- coding: utf-8 -*-
from tornado.web import RequestHandler
import json

class SearchHandler(RequestHandler):
    mapper = {
        'python': 'no.1',
        'java': 'no.2'
    }

    def get(self):
        html = """
            <h3>搜索 %s 结果</h3>
            <p>
                %s
            </p>
        """
        wd = self.get_query_argument('wd')
        result = self.mapper.get(wd)

        # self.write(html % (wd, result))
        resp_result = {
            'wd': wd,
            'result': result
        }
        self.write(json.dumps(resp_result))
        self.set_header("Content-Type", "application/json;charset=utf-8")  # 设置响应头
        self.set_status(200)  # 设置响应状态码
        # 设置cookie
        self.set_cookie("wd", wd)