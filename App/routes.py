from flask import render_template
from App import app

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
	return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def register():
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
def edit_profile()
	return render_template('edit-profile.html')