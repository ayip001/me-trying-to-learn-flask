from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

# @app.route('/')
# @app.route('/index')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
                           title = 'Sign in',
                           form = form)
