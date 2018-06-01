# 我的Flask基础框架

### 初始化数据库
python manager.py db init<br>
python manager.py db migrate<br>
python manager.py db upgrate<br>

<br>

### 运行服务器(Flask-script的默认命令)
python manager.py runserver

<br>

### 运行shell---查看app, db等
python manager.py shell

<br>

# 部署
### 一. 虚拟环境virtualenv：
1.sudo pip insatll virtualenv <br>
2.virtualenv venv <br>
3.source venv/bin/activate <br>
4.(venv) pip insatll -r requirements.txt <br>
5.deactivate <br>

### 二. supervisor
1.sudo apt-get install supervisor <br>
2.vim /etc/supervisor/supervisord.conf <br>
在配置文件中，最后一行加入，表示只要我们的配置文件在以下目录：<br>
[include] <br>
files = /etc/supervisor/conf.d/*.conf <br>
3.sudo vim /etc/supervisor/conf.d/app.conf <br>
[program:fwg] <br>
command=/home/ubuntu/www/fwg/venv/bin/gunicorn manager:app -c /home/ubuntu/www/fwg/gunicorn.conf <br>
directory=/home/ubuntu/www/fwg <br>
autostart=true <br>
autorestart=true <br>
stdout_logfile=/home/ubuntu/www/fwg/logs/gunicorn_supervisor.log <br>                                                 
4.进入supervisor的控制台supervisorctl，可以看到app已经running了 <br>
sudo supervisorctl
app
5.之后可以通过stop app停止app, status来查看。再次启动start app。退出exit
6.supervisor 是服务端，而supervisorctl 是客户端。所以要先确保服务端启动：
service supervisor start / stop.....
7.要在工程目录下创建一个log目录给 supervisor存放log用

### 三.gunicorn
1.安装在venv中,见requirements.txt <br>
2.配置gunicorn文件：/home/ubuntu/www/fwg/gunicorn.conf <br>
工作进程数为3  <br>
workers = 3  <br>
绑定本地8000端口  <br>
bind = '127.0.0.1:8080'<br>

### 四.nginx的配置
1.启动 sudo service nginx status <br> 
2.进入/etc/nginx <br>
注意其中的site-availabe和sites-enable 这2个目录 <br>
site-availabe放的是可用的配置文件 <br>
sites-enable 放的是生效的配置文件 <br>
所以只要在site-availabe创建配置文件，然后再sites-enable 创建软连接即可 <br>
3.创建配置文件----- 注意需要修改或者删除默认的default文件 <br>
sudo vim sites-available/fwg_site  <br>
server {<br>
        listen 80;<br>
        location /static {<br>
                alias /home/ubuntu/www/fwg/static;<br>
        }<br>
        location / {<br>
                proxy_pass http://127.0.0.1:8080;<br>
        }<br>
}<br>
4.创建软连接：sudo ln -s ../sites-available/todo_app . <br>
5.重新加载配置，并重启nginx<br>
sudo service nginx reload <br>
6.如果有错误可以查看日志： <br>
access_log /var/log/nginx/access.log <br>
error_log /var/log/nginx/error.log <br>


