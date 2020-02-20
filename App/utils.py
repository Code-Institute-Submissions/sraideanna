from datetime import datetime, timedelta
import timeago
import dateutil.parser
from operator import itemgetter

from App import app, db

# A function to get recent database activity for the sidebar

def get_recent_activity():
    """ Get current time"""
    now = datetime.now() + timedelta(seconds=60 * 3.4)
    date = datetime.now()
    time_ago = timeago.format(date, now)
    """ Query mongodb for 5 most recent updates, targetting date field and sorting """
    last_five = list(db.streets.find({}, {'name_en': 1, 'translations': 1, '_id': 0}).limit(
        5).sort('translations.date_posted', -1))
    """ Some streets have multiple translations in a list field that must be unpacked before further sorting """
    recent = []
    for obj in last_five:
        for obj1 in obj['translations']:
            recent.append(obj1)
    """ A final sorting and limiting list to five """
    recent = sorted(recent, key=itemgetter('date_posted'), reverse=True)
    recent = recent[:5]
    """ Add time stamp (time ago) to each translation """
    for translation in recent:
        date_posted = timeago.format(translation['date_posted'], now)
        translation['date_posted'] = date_posted
    return recent