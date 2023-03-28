# -*- coding: utf-8 -*-

from tornado.web import Application
from app.views.index_v import IndexHandler
from app.views.cookie_v import CookieHandler
from app.views.order_v import OrderHandler
from app.views.search_v import SearchHandler


def make_app(host='localhost'):
    return Application([
        ('/', IndexHandler),
        ('/search', SearchHandler),
        ('/cookie', CookieHandler),
        (r'/order/(?P<order_id>\d+)/(?P<action_code>\d+)', OrderHandler)
    ], default_host=host)