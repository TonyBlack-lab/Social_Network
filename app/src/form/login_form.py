from flask_wtf import FlaskForm
from werkzeug.routing import ValidationError
from wtforms import IntegerField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from app.src.entity.user import User

class LoginForm(FlaskForm):
    user_number = IntegerField('User number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

    def validate_user_number(self, user_number):
        user = User.query.filter_by(user_number=user_number.data).first()
        if user is None:
            raise ValidationError('Please registered in the system.')