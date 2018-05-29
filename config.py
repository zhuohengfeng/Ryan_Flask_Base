#encoding: utf-8

import sys

# Configuration
DEBUG = True
SECRET_KEY = 'hard to guess string'

# 数据库只要以下设置就可以使用Flask-SQLAlchemy了，会自动判断是sqlite类型
# 这里要写上绝对路径，相对路径搞不懂.....
import os, sys
ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)))
DATABASE_PATH = os.path.join(ABSPATH, 'app.db')
print(DATABASE_PATH)
SQLALCHEMY_DATABASE_URI = r'sqlite://{}'.format(DATABASE_PATH)
#print(SQLALCHEMY_DATABASE_URI)
SQLALCHEMY_TRACK_MODIFICATIONS = False