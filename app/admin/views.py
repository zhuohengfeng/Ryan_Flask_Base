from flask import render_template, redirect, url_for, request,session
from app.admin import admin

@admin.route('/')
def index():
    print("This is admin!!!!")
    return render_template('index.html')
