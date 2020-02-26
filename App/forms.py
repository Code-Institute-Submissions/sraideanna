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


class TranslationForm(FlaskForm):
    translation = StringField('Your Translation:', validators=[DataRequired()])
    note = TextAreaField('Note:', validators=[DataRequired()])
    source = RadioField('What\'s the source for the translation?', choices=[
                        ('user', 'Myself'), ('other', 'Other')], default='user', validators=[DataRequired()])
    src = StringField('Source details:', validators=[Length(max=100)])
    submit = SubmitField('Submit')
    # The following validator prevents a user uploading a translation already held in the db

    def validate_translation(self, translation):
        trans = db.streets.find_one(
            {'translations.name_ga': translation.data})
        if trans:
            raise ValidationError(
                'Sorry, the same translation has already been provided by another user.')


class EditTranslationForm(FlaskForm):
    translation = StringField('Your Translation:', validators=[DataRequired()])
    note = TextAreaField('Note:', validators=[DataRequired()])
    source = RadioField('What\'s the source for the translation?', choices=[
                        ('user', 'Myself'), ('other', 'Other')], default='user', validators=[DataRequired()])
    src = StringField('Source details:', validators=[Length(max=100)])
    submit = SubmitField('Edit')


class EditProfileForm(FlaskForm):
	email = StringField('Edit your email address:',
	                    validators=[DataRequired(), Email()])
	bio = TextAreaField(
	    'Edit your public bio: (optional)')
	location = StringField('Update your location:',
	                         validators=[DataRequired()])
	level = RadioField('Update your translation skill level:', choices=[('master', 'Mastery: Master translator, professional level'), (
	    'enthusiast', 'High-Level Enthusiast: A seasoned translator'), ('amateur', 'Amateur: Some experience but no expert'), ('novice', 'Novice: Little to no experience')], validators=[DataRequired()])
	submit = SubmitField('Edit profile')


	def validate_email(self, email):
	    user = db.users.find_one({'email': email.data})
	    if user and user['username'] != current_user.username:
	        raise ValidationError(
	            'Sorry, an account already exists for that email address.')


class RequestResetPasswordForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        email = db.users.find_one({'email': email.data})
        if email is None:
            raise ValidationError(
                'Sorry, no account is registered with that email address.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Choose a New Password',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')