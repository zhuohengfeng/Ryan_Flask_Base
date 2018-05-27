from flask import render_template, redirect, url_for, request,session
from app.admin import admin

@admin.route('/')
def index():
    print("This is the admin index")
    return render_template('admin.html')
