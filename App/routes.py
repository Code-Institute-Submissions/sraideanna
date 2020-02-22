from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required

import dateutil.parser

from App import app, db, utils
from App.forms import RegistrationForm, LoginForm, StreetSelectForm, TranslationForm, EditProfileForm
from App.models import User, Translation


""" A template filter for use in the profile and your-profile templates (formats date from date obj) """


@app.template_filter('strftime')
def _jinja2_filter_datetime(date, fmt=None):
	date = dateutil.parser.parse(str(date))
	native = date.replace(tzinfo=None)
	format = '%b %d, %Y'
	return native.strftime(format)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
	""" Get data for the recent activity sidebar (in layout.html) """
	recent = utils.get_recent_activity()
	form = StreetSelectForm()
	form.select.choices = [ (item['name_en'], item['name_en']) for item in db.streets.find() ]
	if form.validate_on_submit():
		queryDB = db.streets.find_one({'name_en': form.select.data})
		street_data = {'_id': str(queryDB['_id']), 'name_en': queryDB['name_en'], 'postcode': queryDB['postcode'], 'translations': queryDB['translations'], 'pos': queryDB['pos']}
		""" If street request is valid then return appropriate street page """
		return redirect(url_for('street', street_name=street_data['name_en']))
	return render_template('home.html', form=form, recent=recent)


@app.route('/about')
def about():
	""" Get data for the recent activity sidebar (in layout.html) """
	recent = utils.get_recent_activity()
	return render_template('about.html', title='About Sráideanna', recent=recent)


@app.route('/register', methods=['GET', 'POST'])
def register():
	""" Get data for the recent activity sidebar (in layout.html) """
	recent = utils.get_recent_activity()
	""" If user is logged in, these routes are unnecessary and so redirect to home page"""
	if current_user.is_authenticated:
	    return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
	    user = User(username=form.username.data,
	                email=form.email.data, bio=form.bio.data, location=form.location.data, level=form.level.data, password=form.password.data)
	    user.add_to_db()
	    flash(f'Account created for {form.username.data}! You can now log in.', 'success')
	    return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form, recent=recent)


@app.route('/login', methods=['GET', 'POST'])
def login():
	""" Get data for the recent activity sidebar (in layout.html) """
	recent = utils.get_recent_activity()
	""" If user is logged in, these routes are unnecessary and so redirect to home page """
	if current_user.is_authenticated:
	    return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
	    user = db.users.find_one({'email': form.email.data})
	    if user and user['password'] == form.password.data:
	        user_obj = User(
	            username=user['username'], email=user['email'], bio=user['bio'], location=user['location'], level=user['level'], password=user['password'])
	        login_user(user_obj, remember=form.remember.data)
	        """ The following assures the user will be redirected to the page she wanted before being prompted to sign in (if prompted) """
	        next_page = request.args.get('next')
	        if next_page:
	            return redirect(next_page)
	        else:
	            return redirect(url_for('home'))
	    else:
	        flash('Login Unsuccessful. Please check email and password', 'danger')
	return render_template('login.html', title='Login', form=form, recent=recent)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/street/<street_name>', methods=['GET', 'POST'])
def street(street_name):
	""" Get data for the recent activity sidebar (in layout.html) """
	recent = utils.get_recent_activity()
	user = current_user
	query = street_name
	queryDB = db.streets.find_one({'name_en': query})
	street = {'_id': str(queryDB['_id']), 'name_en': queryDB['name_en'], 'postcode': queryDB['postcode'], 'translations': queryDB['translations'], 'pos': queryDB['pos']}
	return render_template('street.html', title='Street Details', street=street, user=user, recent=recent)


@app.route('/add-translation/<street_name>', methods=['GET', 'POST'])
@login_required
def add_translation(street_name):
	""" Get data for the recent activity sidebar (in layout.html) """
	recent = utils.get_recent_activity()
	user = current_user
	""" Get data from DB """
	street = db.streets.find_one({'name_en': street_name})
	for obj in street['translations']:
	    if obj['username'] == user.username:
	        flash('Translations are limited to one translation per street per user.', 'warning')
	        return redirect(url_for('street', street_name=street['name_en'])) 
	""" Instantiate add translation form """
	form = TranslationForm()
	if form.validate_on_submit():
	    """ Get current time and add to form data """
	    current_date = datetime.now()
	    """ Set src to user if no external source provided """
	    if form.source.data == 'user':
	        form.src.data = current_user.username
	    translation = Translation(name_ga=form.translation.data, date_posted=current_date, note=form.note.data,
	                              src=form.src.data, username=user.username, street_name=street['name_en'])
	    """ Add translation to DB (streets collection) """
	    translation.add_to_db()
	    """ Add translation reference to corresponding user document (users collection) """
	    translation.update_in_user_db()
	    return redirect(url_for('street', street_name=street['name_en']))
	return render_template('add-translation.html', title='Translate Street', form=form, street=street_name, user=user, recent=recent)


@app.route('/edit-translation/<street_name>', methods=['GET', 'POST'])
@login_required
def edit_translation(street_name):
	""" Get data for the recent activity sidebar (in layout.html) """
	recent = utils.get_recent_activity()
	""" Collect street data from query """
	user = current_user
	""" Call DB for street data """
	street_data = db.streets.find_one({'name_en': street_name})
	""" Extract target translation from translations array """
	translation = [translation for translation in street_data['translations'] if translation['username'] == user.username]
	""" Converting list to dict object """
	target_translation = translation[0]
	""" Instantiate edit translation form """
	form = EditTranslationForm()
	""" If request method is GET, then prepopulate the edit form with data from target translation """
	if request.method == 'GET':
	    form.translation.data = target_translation['name_ga']
	    form.note.data = target_translation['note']
	    """ Analysing data to check which radio button to preselect """
	    if target_translation['src'] != target_translation['username']:
	        form.source.data = 'other'
	        form.src.data = target_translation['src']
	    else:
	        form.source.data = 'user'
	""" If method is POST, then validate form and redirect back to the corresponding street page """
	if form.validate_on_submit():
	    """ Get current time and add to form data """
	    current_date = datetime.now()
	    """ Set src to user if no external source provided """
	    if form.source.data == 'user':
	        form.src.data = current_user.username
	    translation = Translation(name_ga=form.translation.data, date_posted=current_date, note=form.note.data,
	                              src=form.src.data, username=user.username, street_name=street_name)
	    """ Update DB to edit translation """
	    translation.update_in_db()
	    return redirect(url_for('street', street_name=street_name))
	return render_template("edit-translation.html", title='Edit your translation', form=form, street=street_name, user=user, recent=recent)


@app.route('/delete-translation/<street_name>', methods=['GET', 'POST'])
def delete_translation(street_name):
	""" Remove translation data from the streets collection and the relational data from the user collection"""
	db.streets.update_one({'name_en': street_name}, { '$pull': { 'translations': { 'username': current_user.username }}})
	db.users.update_one({'username': current_user.username}, { '$pull': { 'translations': { 'street_name': street_name }}})
	return redirect(url_for('street', street_name=street_name))


@app.route('/profile/<user>', methods=['GET', 'POST'])
def view_user_profile(user):
	""" Get data for the recent activity sidebar (in layout.html) """
	recent = utils.get_recent_activity()
	""" If a user is logged on and if the query name matches the logged on user's name, then serve a personal profile template """
	if current_user.is_authenticated and user == current_user.username:
	    image_file = url_for('static', filename='img/avatars/' + current_user.image_file)
	    return render_template('your-profile.html', title='Your Profile', recent=recent, image_file=image_file)
	else:
	    """ Otherwise pull queried user's data from DB, then serve a public profile template """
	    profile_data = db.users.find_one({'username': user})
	    image_file = url_for('static', filename='avatars/' + profile_data['image_file'])
	    return render_template('profile.html', title='User Profile', profile_data=profile_data, recent=recent, image_file=image_file)


@app.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
	""" Get data for the recent activity sidebar (in layout.html) """
	recent = utils.get_recent_activity()
	""" Set avatar image from static avatars folder (will be automated to depend on skill level) """
	image_file = url_for('static', filename='img/avatars/' + current_user.image_file)
	form = EditProfileForm()
	if request.method == 'GET':
	    form.email.data = current_user.email
	    form.bio.data = current_user.bio
	    form.location.data = current_user.location
	    form.level.data = current_user.level
	if form.validate_on_submit():
	    if form.email.data != current_user.email:
	        db.users.update_one({'username': current_user.username}, {
	                        '$set': {'email': form.email.data, 'bio': form.bio.data, 'location': form.location.data, 'level': form.level.data}})
	        flash(f'You\'ve successfully updated your profile. Please log in again.', 'success')
	        return redirect(url_for('logout'))
	    else:
	        db.users.update_one({'username': current_user.username}, {
	                        '$set': {'email': form.email.data, 'bio': form.bio.data, 'location': form.location.data, 'level': form.level.data}})
	        flash(f'You\'ve successfully updated your profile.', 'success')
	        return redirect(url_for('view_user_profile', user=current_user.username))
	return render_template('edit-profile.html', title='Edit your profile', image_file=image_file, recent=recent, form=form)


@app.route("/reset-password", methods=['GET', 'POST'])
def reset_password_request():
    return render_template('reset-password-request.html', title='Reset Password')