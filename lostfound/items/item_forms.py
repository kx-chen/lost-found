from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, validators

class NewItemForm(Form):
    name = StringField('Name of item', [validators.DataRequired(), validators.Length(min=5)])
    details = StringField("Details of item", [validators.DataRequired(), validators.Length(min=5)])
    submit = SubmitField("Submit")