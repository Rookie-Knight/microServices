# -*- coding: utf-8 -*-
from tornado.web import RequestHandler


class OrderHandler(RequestHandler):
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