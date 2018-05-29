#encoding: utf-8

'''
python manage.py db init
初始化一个迁移脚本的环境，只需要执行一次。

python manage.py db migrate
将模型生成迁移文件，只要模型更改了，就需要执行一遍这个命令。这步就会生成db文件。

python manage.py db upgrade
将迁移文件真正的映射到数据库中。每次运行了migrate命令后，就记得要运行这个命令。
这一步会产生数据表。
'''

import os, sys
ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)))
sys.path.append(os.path.join(ABSPATH, 'app','restful'))
print(sys.path)


from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db
# 注意这里也要导入各种模models中的各个模型
from app.models import User, Question


manager = Manager(app)

# 使用Migrate绑定app和db
migrate = Migrate(app, db)

# 添加迁移脚本的命令到manager中
# 使用的时候: python manager.py db xxxx
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
