from app import app, db
from flask import render_template, flash, url_for
from flask_login import current_user, login_user, logout_user
from werkzeug.utils import redirect
from app.forms import RegistForm, LoginForm
from flask_bootstrap import Bootstrap
from app.models import Regist

bootstrap = Bootstrap(app)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistForm()

    if form.validate_on_submit():
        user = Regist(mobile_number=form.mobile_number.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return 'success'

    return render_template('registform.html', title='Rigistration', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if not current_user.is_authenticated:
        if form.validate_on_submit():
            user = Regist.load_from_login(form.user_id_number.data)

            if user is None or not user.check_password(form.password.data):
                flash('Invalid user id number or password')
                return redirect(url_for('login'))

            login_user(user, remember=form.remember_me.data)

            return 'success!'


        return render_template('loginform.html', title='LogIn', form=form)

    return 'success!!!'


@app.route('/logout')
def logout():
    logout_user()
    return 'success'
