#encoding: utf-8

# Configuration
DEBUG = True
SECRET_KEY = 'hard to guess string'

# 数据库只要以下设置就可以使用Flask-SQLAlchemy了，会自动判断是sqlite类型
# 这里要写上绝对路径，相对路径搞不懂.....
SQLALCHEMY_DATABASE_URI = r'sqlite:///D:\5_Python\Ryan_Flask_Base\app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False