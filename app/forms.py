from flask_wtf import FlaskForm
from werkzeug.routing import ValidationError
from wtforms import IntegerField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email
from app.models import Regist


class RegistForm(FlaskForm):
    mobile_number = IntegerField('User mobile number', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    rePassword = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign In')

    def validate_mobile_number(self, mobile_number):
        user = Regist.query.filter_by(mobile_number=mobile_number.data).first()
        if user is not None:
            raise ValidationError('Please use available nomber')

    def validate_email(self, email):
        user = Regist.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class LoginForm(FlaskForm):
    user_id_number = StringField('User id number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

    def validate_user_id_number(self, user_id_number):
        user = Regist.query.filter_by(user_id_number=user_id_number.data).first()
        if user is None:
            raise ValidationError('Please registered in the system.')