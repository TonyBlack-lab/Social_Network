from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm (FlaskForm): # здесь сздается переменная класса для каждого поля,
                             # Каждому полю присваивается описание или метка в качестве первого аргумента
    user_mobile = StringField('User Mobile', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')