#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/1 9:21
# @Author  : zhuo_hf@foxmail.com
# @Site    :
# @File    : 1.py
# @Software: PyCharm
import os
from app import create_app, db
from app.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

# 工厂模式创建app
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


# 往shell中加入context
manager.add_command("shell", Shell(make_context=make_shell_context))
# 数据库迁移命令
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
