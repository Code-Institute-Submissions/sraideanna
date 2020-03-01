# Database Organisation

## Overview
Sráideanna! uses a document-oriented database using MongoDB. The chosen structure was developed by progessing through the following steps:

### What does the application do, and how does that shape the database?
Well, the application allows **users** to look up **streets** and their Irish language **translations**, so the database has to provide lists or collections of each of these elements.

### What data for what document in what collection?
The application depends on users so best to begin there. 

* A sample 'user' object from the **Users** collection in the database:

```
'user': {
	'_id': ObjectId('5e46725c01ce9d57dc8a23d1'),
	'username': 'roro',
	'email': 'roro@mail.com',
	'bio': 'I am a fluent Irish speaker with a long-time interest in local place-names, their history and meaning. I'm an amateur translator, but I know how to do research to find appropriate translations for street names in Belfast and beyond.',
	'location': 'Paris',
	'level': 'amateur',
	'password': 'goa',
	'translations': [
						{
							'street_name': 'Airport Road',
							'date_posted': '2020-02-14T12:46:42.547+00:00'
						},
						{
							'street_name': 'Falls Road',
							'date_posted': '2020-02-14T12:59:12.337+00:00'
						},
					],
	'favourites': [],
	'image_file': 'default.jpg'
}
```

The 'user' document object contains login data, basic profile data, some unexploited data for future features, and importantly, a 'translations' array field for the user's translations. The actual translations aren't held here, however. These are just very simplified <em>references</em> to them, containing only the English-language 'street_name' and the date the translation was posted. The actual translations have been appended to the 'street' document object in the **streets** collection. See below. 

* A sample 'street' object from the **Streets** collection in the database:

```
'street': {
	'_id': ObjectId('5e3c9d20061b1ddbf630ee66'),
	'name_en': 'Abbey Gardens',
	'pos': [
		'54.5920096',
		'-5.8367929'
	],
	'postcode': 'BT5 7HL',
	'translations': [
						{
							'name_ga': 'Garraithe na Mainistreach',
							'date_posted': '2020-02-27T12:49:32.745+00:00',
							'note': 'Literal translation - "gardens of the abbey".',
							'src': 'roro',
							'username': 'roro',
							'street_name': 'Abbey Gardens'
						}
					]
}

```

As is clear in the sample above, the **translations** entity was incorporated into the **streets** collection, appended as a list / array to the 'street' object. Why so? Well, the database of Irish names (translations) is far from complete, and the (at least initial) core of the application is the index of Belfast street names in English. It would be easy to envisage a reorganisation of the database when (if!) the translations database is complete - a full database and some reorganisation would allow reverse searching (Irish to English), for example.

Until then, however, the translations are children of the streets they translate. They contain all the data necessary to constructing a coherent database. The 'username' field allows for easy cross-referencing to the **Users** collection, while the 'street_name' field on the 'user' document serves the same purpose in the other direction.

Note that the application will change the 'username' value to 'Account Deleted' if the user deletes their account. This assures the persistence of their data but the disassociation of it from them. I imagine a production version of this app would need to spell out the legal terms and conditions.

## Conclusions
This organisation of the data facilitated easy interaction with it when it came to all the basic 'crud' operations. More complex operations such as sorting cursors or accessing nested data or such like are also very straightforward with the document-oriented database. Relationships are expressed cleanly by reference. In the application itself, some database operations are written as class methods but more often they are incorporated into the route functions.

## Future Development
Refine database management. Using indexes on street names, for example, or making use of the aggregation framework to optimise data flow more generally.






* Back to [README](../../README.md).
* Jump to [testing documentation](../docs/testing.md).
