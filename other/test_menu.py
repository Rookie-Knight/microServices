# -*- coding: utf-8 -*-
from unittest import TestCase

from utils.conn import session, Base
from app.models.menu import Menu


class TestMenuORM(TestCase):

    def test_create(self):
        Base.metadata.drop_all()
        Base.metadata.create_all()

    def test_add(self):
        m1 = Menu()
        m1.title = '用户管理'

        session.add(m1)
        session.commit()

    def test_adds(self):
        session.add_all([
            Menu(title="订单管理"),
            Menu(title="会员管理", url="/user1", parent_id=1),
            Menu(title="派件员", url="/user2", parent_id=1),
            Menu(title="合作商", url="/user3", parent_id=1),
            Menu(title="订单统计", url="order_cnt", parent_id=2)
        ])
        session.commit()

    def test_get(self):
        # 查询：session.query(模型类)
        m = session.query(Menu).get(1)
        print(m.title)
        print("--查看所有的子菜单--")
        for cm in m.children:
            print(cm.title)

    def test_query_root_menu(self):
        # 查看所有的一级菜单
        # root_menus = session.query(Menu).filter_by(parent_id=None)
        root_menus = session.query(Menu).filter(Menu.parent_id.is_(None)).all()
        for menu in root_menus:
            print(menu.title)
            # 查看二级菜单
            for sub_menu in menu.children:
                print("-", sub_menu.title)

    def test_update(self):
        menu = session.query(Menu).get(5)
        print(menu.title)
        menu.title = "合作伙伴"
        session.add(menu)
        session.commit()

    def test_delete(self):
        menu = session.query(Menu).get(5)
        session.delete(menu)
        session.commit()