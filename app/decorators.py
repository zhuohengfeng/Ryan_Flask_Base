#encoding: utf-8
from flask import redirect, url_for, session
import functools

#登录限制的装饰器
def login_reuired(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user_id'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper
