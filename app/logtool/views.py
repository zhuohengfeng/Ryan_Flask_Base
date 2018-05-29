from flask import render_template, redirect, url_for, request,session
from app import app

@app.route('/log/')
def index():
    return "this is the log test"
