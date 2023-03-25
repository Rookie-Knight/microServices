# coding:utf-8
import tornado.web
import tornado.ioloop
import tornado.options
from tornado.httputil import HTTPServerRequest


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        """获取数据"""
        # 请求参数读取
        # get_argument和get_arguments在GET,POST...请求方式中都通用
        # get_query_argument 和 get_query_arguments 只适用于GET请求的查询参数

        # 1.读取单个参数
        wd = self.get_argument('wd')
        print(wd)
        # 2.读取多个参数名相同的参数值
        titles = self.get_arguments("title")
        print(titles)
        self.write("<h3>Hello Tornado</h3>")
        # 3.从查询参数中读取url路径参数
        wd2 = self.get_query_argument('wd')
        print(wd2)
        titles2 = self.get_query_arguments("title")
        print(titles2)
        # 4.从请求对象中读取参数(不建议使用)
        # request请求对象的所有属性都是字典格式，字典里边key对应的value都是bytes字节类型
        # 变量名：变量类型 = xxx的方式是Python3.5以上的Type Hint语法，非强制性
        req: HTTPServerRequest = self.request
        wd3 = req.arguments.get('wd')
        print(wd3)

        wd4 = req.query_arguments.get('wd')
        print(wd4)

    def post(self):
        """提交数据"""
        name = self.get_body_argument('name')
        city = self.get_body_argument('city')
        print(name, city)
        self.write("<h3>Post请求</h3>")

    def put(self):
        """提交数据"""
        self.write("<h3>Put请求</h3>")

    def delete(self):
        """提交数据"""
        self.write("<h3>Delete请求</h3>")

def make_app():
    return tornado.web.Application([
        ('/', IndexHandler)
    ], default_host=tornado.options.options.host)

if __name__ == '__main__':
    # 定义命令行参数
    tornado.options.define("port",
                           default=8000,
                           type=int,
                           help="bind socket port"
                           )
    tornado.options.define("host",
                           default="localhost",
                           type=str,
                           help="set host"
                           )
    # 解析命令行参数
    tornado.options.parse_command_line()
    app = make_app()
    app.listen(tornado.options.options.port)

    print("starting http://%s:%s" % (tornado.options.options.host, tornado.options.options.port))
    tornado.ioloop.IOLoop.current().start()