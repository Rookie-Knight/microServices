# -*- coding: utf-8 -*-
import os

from tornado.web import Application

from app.ui.menu import MenuModule
from app.views.index_v import IndexHandler
from app.views.cookie_v import CookieHandler
from app.views.order_v import OrderHandler
from app.views.search_v import SearchHandler
from app.views.downloader import DownloadHandeler

# 工程目录
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
settings = {
    'debug': True,
    'template_path': os.path.join(BASE_DIR, "templates"),
    'static_path': os.path.join(BASE_DIR, "static"),
    'static_url_prefix': "/s/",
    'ui_modules': {
        'Menu': MenuModule
    }
}


def make_app(host='localhost'):
    # print(settings.get("template_path"))
    return Application([
        ('/', IndexHandler),
        ('/search', SearchHandler),
        ('/cookie', CookieHandler),
        (r'/order/(?P<order_id>\d+)/(?P<action_code>\d+)', OrderHandler),
        (r'/download', DownloadHandeler)
    ], default_host=host, **settings)