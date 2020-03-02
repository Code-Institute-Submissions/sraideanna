from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from App import PyMongo, db, login_manager, app
from bson.objectid import ObjectId


class User:

    def __init__(self, username, email, bio, location, level, password, translations=[], favourites=[], image_file='default.jpg'):
        self.username = username
        self.email = email
        self.bio = bio
        self.location = location
        self.level = level
        self.password = password
        self.translations = translations
        self.favourites = favourites
        self.image_file = image_file

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.bio}', '{self.location}', '{self.level}', '{self.translations}', '{self.favourites}', '{self.image_file}')"

    """ The following 4 methods are necessary for the flask-login functionality """
    @login_manager.user_loader
    def load_user(username):
        user = db.users.find_one({'username': username})
        if user:
            return User(username=user['username'], email=user['email'], bio=user['bio'], location=user['location'], level=user['level'], password=user['password'], translations=user['translations'], favourites=user['favourites'])
        else:
            return None

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    """ A bit of a hack to make login-manager work with mongo (uses username rather than id)! """

    def get_id(self):
        return self.username

    def add_to_db(self):
        db.users.insert_one({'username': self.username, 'email': self.email, 'bio': self.bio, 'location': self.location, 'level': self.level,
                             'password': self.password, 'translations': self.translations, 'favourites': self.favourites, 'image_file': self.image_file})

    def get_password_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'username': self.username}).decode('utf-8')

    """ A static method that allows for verification of reset password token """

    @staticmethod
    def verify_password_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            username = s.loads(token)['username']
        except:
            return None
        return db.users.find_one({'username': username})


class Translation:

    def __init__(self, name_ga, date_posted, note, src, username, street_name):
        self.name_ga = name_ga
        self.date_posted = date_posted
        self.note = note
        self.src = src
        self.username = username
        self.street_name = street_name

    def __repr__(self):
        return f"Translation('{self.name_ga}', '{self.date_posted}', '{self.note}', '{self.src}', '{self.username}', '{self.street_name}')"

    """ Methods for interacting with the db """

    def add_to_db(self):
        db.streets.update_one({'name_en': self.street_name}, {'$addToSet': {'translations': {
                              'name_ga': self.name_ga, 'date_posted': self.date_posted, 'note': self.note, 'src': self.src, 'username': self.username, 'street_name': self.street_name}}})

    def update_in_db(self):
        db.streets.update_one({'name_en': self.street_name, 'translations.username': self.username}, {'$set': {'translations.$.name_ga': self.name_ga,
                                                                                                               'translations.$.date_posted': self.date_posted, 'translations.$.note': self.note, 'translations.$.src': self.src, 'translations.$.username': self.username}})

    def update_in_user_db(self):
        db.users.update_one({'username': self.username}, {
                            '$addToSet': {'translations': {'street_name': self.street_name, 'date_posted': self.date_posted}}})
