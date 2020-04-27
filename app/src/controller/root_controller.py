from flask import render_template, flash, url_for
from flask_login import current_user, login_user, logout_user
from werkzeug.utils import redirect

from flask_bootstrap import Bootstrap

from app.src import app, db
from app.src.entity.user import User
#from app.src.form.sign_in_form import SignInForm
#from app.src.form.sign_up_form import SignUpForm

bootstrap = Bootstrap(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', is_auth=current_user.is_authenticated)

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistForm()

    if form.validate_on_submit():
        user = User(mobile_number=form.mobile_number.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        login_user(user)
        return redirect(url_for('index'))

    return render_template('registration.html', title='Rigistration', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if not current_user.is_authenticated:
        if form.validate_on_submit():
            user = User.load_from_user_number(form.user_number.data)

            if user is None or not user.check_password(form.password.data):
                flash('Invalid user number or password')
                return redirect(url_for('login'))

            login_user(user, remember=form.remember_me.data)

            return redirect(url_for('index'))

        return render_template('login.html', title='LogIn', form=form)

    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))