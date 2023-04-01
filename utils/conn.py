# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://root:6666@192.168.3.19:3306/tornado_test_db?charset=utf8")

# 生成数据库连接的类
DbSession = sessionmaker(bind=engine)

# 创建会话类对象
session = DbSession()

# 生成所有模型类的父类
Base = declarative_base(bind=engine)
