from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
#from werkzeug.utils import


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm() # просто передает объект формы
    if form.validate_on_submit(): # метод обработки всей формы
        flash('Login request for user_mobile {}, remember_me={}'.format(
            form.user_mobile.data, form.remember_me.data))
    return render_template('login.html', title='Sign In', form=form)


@app.route ('/community')
def community():
    user = {'nickname': 'приятель'} # выдуманный пользователь/приветствие
    posts = [ # список выдуманных постов
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Poland'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was cool'
        }
    ]

    return render_template("community.html",
                            title="Home",
                            user=user,
                            posts=posts)
