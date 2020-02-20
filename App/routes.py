from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required

from App import app, db, utils
from App.forms import RegistrationForm, LoginForm, StreetSelectForm
from App.models import User, Translation





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


@app.route('/street/<street_name>', methods=['GET', 'POST'])
def street(street_name):
	return render_template('street.html')


@app.route('/add-translation/<street_name>', methods=['GET', 'POST'])
def add_translation(street_name):
	return render_template('add-translation.html')


@app.route('/edit-translation/<street_name>', methods=['GET', 'POST'])
def edit_translation(street_name):
	return render_template('edit-translation.html')


@app.route('/delete-translation/<street_name>', methods=['GET', 'POST'])
def delete_translation(street_name):
	return redirect(url_for('street'))


@app.route('/profile/<user>', methods=['GET', 'POST'])
def view_user_profile(user):
	return render_template('profile.html')


@app.route('/edit-profile', methods=['GET', 'POST'])
def edit_profile():
	return render_template('edit-profile.html')


@app.route("/reset-password", methods=['GET', 'POST'])
def reset_password_request():
    return render_template('reset-password-request.html', title='Reset Password')