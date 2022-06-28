from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    #email, password, submit_button
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField ('Password', validators = [DataRequired()])
    favorite_car = StringField('Favorite Car')
    submit = SubmitField()