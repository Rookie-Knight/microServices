# -*- coding: utf-8 -*-

from tornado.web import UIModule
from utils.conn import session
from app.models.menu import Menu

class MenuModule(UIModule):

    def render(self):
        # 准备数据（从缓存/从数据库..)
        data = {
            # 'menus': [
            #     {"title": "百度", "url": "https://www.baidu.com/"},
            #     {"title": "京东", "url": "https://jd.com"},
            #     {"title": "淘宝", "url": "http://www.taobao.com"}
            # ]
            'menus': session.query(Menu).filter_by(parent_id=None).all()

        }
        # 渲染ui模块的模板
        return self.render_string('ui/menu.html', **data)