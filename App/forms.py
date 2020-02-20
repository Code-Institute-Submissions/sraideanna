from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField, SelectField, DateField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired
from App import db
from flask_login import current_user


class RegistrationForm(FlaskForm):
	username = StringField('Username:', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email:', validators=[DataRequired(), Email()])
	bio = TextAreaField('If you want to, tell the community a bit about yourself: (optional)')
	location = StringField('Your location:', validators=[DataRequired()])
	level = RadioField('What is your level of translation ability in Irish?', choices=[('master', 'Mastery: Master translator, professional level'), (
	    'enthusiast', 'High-Level Enthusiast: A seasoned translator'), ('amateur', 'Amateur: Some experience but no expert'), ('novice', 'Novice: Little to no experience')], validators=[DataRequired()])
	password = PasswordField('Choose a Password:', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password:',
	                                 validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

	def validate_username(self, username):
	    user = db.users.find_one({'username': username.data})
	    if user:
	        raise ValidationError(
	            'Sorry, the username you chose is already taken. Please choose another.')

	def validate_email(self, email):
	    email = db.users.find_one({'email': email.data})
	    if email:
	        raise ValidationError(
	            'Sorry, an account already exists for that email address.')


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')


class StreetSelectForm(FlaskForm):
	select = SelectField('', choices=['Abbey Gardens', 'Abercorn Street'], validators=[DataRequired(), InputRequired()])
	submit = SubmitField('Select')