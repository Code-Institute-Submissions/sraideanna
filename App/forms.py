from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField, SelectField, DateField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired
from App import db
from flask_login import current_user


class StreetSelectForm(FlaskForm):
    select = SelectField('', choices=['Abbey Gardens', 'Abercorn Street'],
                         validators=[DataRequired(), InputRequired()])
    submit = SubmitField('Select')