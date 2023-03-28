# -*- coding: utf-8 -*-
from tornado.web import RequestHandler


class CookieHandler(RequestHandler):

    def get(self):
        # 从查询参数中读取Cookie的名称
        if self.request.arguments.get('name'):
            name = self.get_query_argument('name')
            print("name:", name)
            # 如果cookie的键不存在，返回None
            cookie = self.get_cookie(name)
            self.write(cookie)
        else:
            # 显示所有cookie
            cookies = self.request.cookies
            html = '<ul>%s</ul>'
            cookie_list = []
            for cookie in cookies.keys():
                cookie_list.append("<li>%s: %s</li>" % (cookie, self.get_cookie(cookie)))
            self.write(html % ''.join(cookie_list))

    def delete(self):
        """删除cookie"""
        name = self.get_argument("name")
        if self.request.cookies.get(name, None):
            # 删除cookie
            self.clear_cookie(name)
            self.write("<h3 style='color:green'>删除cookie %s 成功</h3>" % name)
        else:
            self.write("<h3 style='color:red'>删除cookie %s 失败</h3>" % name)

        # 重定向操作时，不需要再调用self.write(),即使调用了也不会在浏览器上显示
        self.redirect("/cookie")