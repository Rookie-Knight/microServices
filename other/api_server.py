# -*- coding: utf-8 -*-
import uuid

from tornado.web import RequestHandler
from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.options import options, define, parse_command_line
import json


class LoginHandler(RequestHandler):
    users = [
        {
            "id": 1,
            "name": "thor",
            "pwd": "123",
            "last_login_device": "android 12 HUAWEI P60"
        }
    ]

    def get(self):
        # # 获取json数据,通过当前对象的request对象属性的body属性来获取json数据
        # data = self.request.body
        # # print(data)
        # # print(self.request.headers.get("Content-Type"))
        #
        # # 从请求头中获取上传的数据的数据类型
        # content_type = self.request.headers.get("Content-Type")
        # if content_type.startswith("application/json"):
        #     # 将字节码转化成utf8编码格式
        #     json_str = data.decode("utf-8")
        #     # 反序列化
        #     json_data = json.loads(json_str)
        #     # 响应数据
        #     resp_data = {}
        #     # 检测用户名和口令是否正确
        #     for user in self.users:
        #         if json_data.get("name") == user["name"] \
        #                 and json_data.get("pwd") == user["pwd"]:
        #             resp_data["msg"] = "success"
        #             resp_data["token"] = uuid.uuid4().hex
        #             break
        #     else:
        #         resp_data["msg"] = "login error"
        #
        #     self.set_header("Content-type", "application/json")
        #     self.write(json.dumps(resp_data))  # write()函数可接收str, dict, list
        #
        # else:
        #     self.write("the data you upload must be json")
        pass

    def set_default_headers(self):
        # 前端使用基于cors的跨域请求时
        # 所有的请求方法执行后，默认设置的响应头信息
        # 以下设置响应头都是解决跨域问题
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Content-Type, x-requested-with")
        self.set_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE")

    def post(self):
        # 前端使用post请求跨域登录
        # 获取前端发送的json数据,该数据是字节类型
        json_str = self.request.body
        # 将json数据反序列化
        request_data = json.loads(json_str.decode("utf-8"))

        resp_data = {}
        # 校验数据
        for user in self.users:
            if request_data["name"] == user["name"] \
                    and request_data["pwd"] == user["pwd"]:
                        resp_data["msg"] = "success"
                        resp_data["token"] = uuid.uuid4().hex
            else:
                resp_data["msg"] = "login error"

            self.set_header("Content-Type", "application/json")
            self.write(resp_data)

    def put(self):
        pass

    def delete(self):
        pass

    def options(self):
        # 跨域请求时，会被客户端请求，用来表示服务器是否支持跨域请求
        self.set_status(200)



def make_app():
    return Application([
        ('/user', LoginHandler)
    ], default_host=options.host)


if __name__ == '__main__':
    define("port", default=8000, type=int, help='绑定的端口')
    define("host", default="localhost", type=str, help='绑定的主机IP')

    parse_command_line()  # 解析命令行参数
    app = make_app()
    app.listen(options.port)

    print("starting http://%s:%s" % (options.host, options.port))
    IOLoop.current().start()
