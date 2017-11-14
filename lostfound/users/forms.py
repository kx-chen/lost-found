from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField

class SignupForm(Form):
    firstname = StringField('First Name')
    lastname = StringField('Last Name')
    email = StringField('Email')
    password = PasswordField('Password')
    submit = SubmitField("Register")

class SigninForm(Form):
    email = StringField('Email')
    password = PasswordField('Password')
    submit = SubmitField("Sign In")