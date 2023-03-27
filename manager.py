# coding:utf-8
import tornado.web
import tornado.ioloop
import tornado.options
import json
from tornado.httputil import HTTPServerRequest


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        """获取数据"""
        # 请求参数读取
        # get_argument和get_arguments在GET,POST...请求方式中都通用
        # get_query_argument 和 get_query_arguments 只适用于GET请求的查询参数
        # get请求参数要全部传递对，否则报400 bad request 错误
        # 1.读取单个参数
        wd = self.get_argument('wd')
        print(wd)
        # 2.读取多个参数名相同的参数值
        titles = self.get_arguments("title")
        print(titles)
        # self.write("<h3>Hello Tornado</h3>")
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
        # 读取表单参数
        # 方式1：任何请求方式都可以获取
        # name = self.get_argument('name')
        # city = self.get_argument('city')
        # 方式2：在Post请求时建议使用这种
        name = self.get_body_argument('name')
        city = self.get_body_argument('city')
        # 方式3：
        req = self.request
        name = req.arguments.get('name').decode('utf-8')
        city = req.arguments.get('city').decode('utf-8')
        print(name, city)
        self.write("<h3>Post请求</h3>")

    def put(self):
        """提交数据"""
        self.write("<h3>Put请求</h3>")

    def delete(self):
        """提交数据"""
        self.write("<h3>Delete请求</h3>")


class SearchHandler(tornado.web.RequestHandler):
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


class CookieHandler(tornado.web.RequestHandler):

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


class OrderHandler(tornado.web.RequestHandler):
    goods = [
        {
            "id": "1",
            "name": "哈利波特",
            "author": "JK罗琳",
            "price": 180
        },
        {
            "id":"2",
            "name": "龙族",
            "author": "江南",
            "price": 80
        }

    ]

    action_map = {
        1: "取消订单",
        2: "再次购买",
        3: "评价"
    }

    def query(self, order_id):
        for good in self.goods:
            if good.get("id") == order_id:
                return good

    def initialize(self):
        # 所有的请求方法在调用之前，都会进行初始化操作
        print("-----initialize-----")

    def prepare(self):
        # 在初始化之后，调用行为方法之前，调用此方法进行预处理
        print("-----prepare-----")

    def on_finish(self):
        # 在行为方法调用之后调用，可用于释放资源
        print("--on_finish--")


    def get(self, order_id, action_code):
        html = """
            <p>
                商品编号：%s
            </p>
            <p>
                商品名称：%s
            </p>
                商品价格：%s
            <p>
            </p>
        """
        print("---Get---")
        good = self.query(order_id)
        self.write("<h3>订单查询</h3>")
        self.write(html % (good.get("id"), good.get("name"), good.get("price")))
        self.write(self.action_map.get(int(action_code)))

    def post(self, order_id, action_code):
        print("---POST---")
        self.write("---POST---")


def make_app():
    return tornado.web.Application([
        ('/', IndexHandler),
        ('/search', SearchHandler),
        ('/cookie', CookieHandler),
        (r'/order/(?P<order_id>\d+)/(?P<action_code>\d+)', OrderHandler)
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