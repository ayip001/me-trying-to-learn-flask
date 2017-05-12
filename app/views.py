from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'placeholder user object'} # placeholder user object
    posts = [
        {
            'author': {'nickname': 'friend user 1'},
            'body': 'post 1 lorem ipsum'
        },
        {
            'author': {'nickname': 'friend user 2'},
            'body': 'post 2 foo bar'
        }
    ]
    return render_template('index.html',
                           title = 'Home',
                           user = user,
                           posts = posts)
