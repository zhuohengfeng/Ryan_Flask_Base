from app import app, db
from flask import render_template, redirect, url_for, request,session
from app.models import User, Question
from app.decorators import login_reuired

# args={'a':1,'b':2}
# func(**args)
# 等价于函数调用 func(a=1,b=2)
@app.route('/index')
@app.route('/')
def index():
    context = {
        'questions': Question.query.order_by('-create_time').all()
    }
    return render_template('index.html', **context)

@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        #print("Regist: telephone={}, username={}, password={}, repassword={}".format(telephone, username, password, repassword))
        # 手机号码验证是否已经存在
        user = User.query.filter(User.telephone == telephone).first()
        if user:
            return u"注册失败，手机已经存在"
        else:
            if password != repassword:
                return u"两次输入的密码不相等"
            else:
                user = User(telephone=telephone, username=username, password=password)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = User.query.filter(User.telephone == telephone, User.password == password).first()
        if user:
            session['user_id'] = user.id
            # 如果想在31天内都不需要登录
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return u"手机号码或者密码错误，请确认后再登录"


@app.route('/logout')
def logout():
    if session.get('user_id'):
        session.pop('user_id')
    return redirect(url_for('login'))

@app.route('/question/', methods=['GET', 'POST'])
@login_reuired
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title=title, content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        question.author = user
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('index'))

#可以往模板上下文中注入一个字典
#在flask中被称作上下文处理器，借助app_context_processor我们可以让所有自定义变量在模板中可见
@app.context_processor
def my_context_processor():
    print('app.context_processor')
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user': user}
    return {}