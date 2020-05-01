from flask_wtf import FlaskForm
from werkzeug.routing import ValidationError
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from app.src.entity.user import User

class RegistForm(FlaskForm):
    mobile_number = StringField('Mobile number', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    rePassword = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_mobile_number(self, mobile_number):
        user = User.query.filter_by(mobile_number=mobile_number.data).first()
        if user is not None:
            raise ValidationError('Please use available mobile number')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email')