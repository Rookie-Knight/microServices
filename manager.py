# coding:utf-8

from tornado.ioloop import IOLoop
from tornado.options import define, parse_command_line, options
from app import make_app



if __name__ == '__main__':
    # 定义命令行参数
    define("port",
           default=8000,
           type=int,
           help="bind socket port"
           )
    define("host",
           default="localhost",
           type=str,
           help="set host"
           )
    # 解析命令行参数
    parse_command_line()
    app = make_app(options.host)
    app.listen(options.port)

    print("starting http://%s:%s" % (options.host, options.port))
    IOLoop.current().start()