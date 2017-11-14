from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
class SignupForm(Form):
    email = StringField('email')
    password = PasswordField('password')
    submit = SubmitField("Sign In")