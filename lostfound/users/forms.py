from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, SubmitField, validators


class SignupForm(Form):
    firstname = StringField('First Name',
                            [validators.DataRequired(),
                             validators.Length(min=2)])
    lastname = StringField('Last Name',
                           [validators.DataRequired(),
                            validators.Length(min=2)])
    email = StringField('Email',
                        [validators.DataRequired(),
                         validators.Length(min=2)])
    password = PasswordField('Password',
                             [validators.DataRequired(),
                              validators.Length(min=6)])
    submit = SubmitField("Register")


class SigninForm(Form):
    email = StringField('Email',
                        [validators.DataRequired(),
                         validators.Length(min=2)])
    password = PasswordField('Password',
                             [validators.DataRequired(),
                              validators.Length(min=2)])
    submit = SubmitField("Sign In",
                         [validators.DataRequired(),
                          validators.Length(min=2)])
