from flask_wtf import FlaskForm as Form
from wtforms import StringField, SubmitField, validators, TextAreaField


class NewItemForm(Form):
    name = StringField('Name of item', [validators.DataRequired(), validators.Length(min=5)])
    details = TextAreaField("Details of item", [validators.DataRequired(), validators.Length(min=5)])
    submit = SubmitField("Submit")
