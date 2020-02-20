from flask import render_template, url_for, flash, redirect, request
from App import app, db
from App.forms import StreetSelectForm
from App.models import User
from flask_login import login_user, current_user, logout_user, login_required



@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = StreetSelectForm()
    form.select.choices = [(item['name_en'], item['name_en'])
                           for item in db.streets.find()]
    if form.validate_on_submit():
        queryDB = db.streets.find_one({'name_en': form.select.data})
        street_data = {
            '_id': str(queryDB['_id']), 'name_en': queryDB['name_en'], 'postcode': queryDB['postcode'], 'translations': queryDB['translations'], 'pos': queryDB['pos']}
        """ ---------------- """
        return redirect(url_for('street', street_name=street_data['name_en']))
    return render_template('home.html', form=form)


@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
	return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
	return render_template('login.html')


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
def view_profile(user):
	return render_template('profile.html')


@app.route('/edit-profile', methods=['GET', 'POST'])
def edit_profile():
	return render_template('edit-profile.html')