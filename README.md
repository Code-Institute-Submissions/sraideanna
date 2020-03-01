# Sráideanna!
A collaborative space where users can look up the Irish language version of Belfast street-names, or even better - sign up and start contributing translations in order to complete the database.

\
\
\
![](/App/static/img/homepage.png)
<br />
<br />
**Click here to see a working [demo](https://sraideanna.herokuapp.com/).**
<br />
<br />
<br />

## Overview
 
### What is this application for?
Unlike in the south of Ireland, here in the north there is no one place where people can learn the Irish language version of their street-name. There are some resources, but they are incomplete and scattered across a variety of databases or web-sites. A lot of translating work has not been done.

**Sráideanna** is a platform that seeks to address that problem. The application is designed for use by a community of committed Irish-language speakers who will complete the database to make sure that all the city's inhabitants have a place to go to learn about the Gaelic origins of the place they live.

### What does it do?
Users can search the **Sráideanna!** database upon their first use of the application. No registration is necessary to search and consult entries in the database. 

Users who are interested can sign up (using a valid email address) in order to become **community members** and to contribute translations of their own.

**Community Members** are asked to register profile details about their skill level in Irish, their location (i.e. the name of a city or town), and a short public biography. Members can, of course, edit their profiles (including log-in details) at any time after registration.

### How does it work
 
**Sráideanna** is built using the python-based **Flask** micro-framework. 

**PyMongo** is used to connect the application's Python classes and methods to a **MongoDB** database. All data input is handled using **WTForms**.

The site is styled using the **Bootstrap CSS** front-end framework for responsiveness and enhanced user-experience. **JQuery** and **Popper** are dependencies of Bootstrap. 

The application is hosted on the **Heroku** platform, the database is hosted by **MongoDB Atlas**. 

The **MONGO_URI** and **SECRET_KEY** are hidden in environment variables locally during development and stored as environment variables using Heroku Config Vars in production. 

The site is designed using a **mobile-first** approach and a live demo can be viewed [HERE](https://sraideanna.herokuapp.com/). 

## Features
The following are the features provided in the Sráideanna! application. 

### Existing Features

> please note that Sráideanna does not yet include authentication for user login

#### Basic Features
* Unregistered users can search the database, consult street pages and public user profiles. A user who is not logged in will be redirected to the login page if they attempt to add translations.

#### User Registration
* Committed users can register in order to contribute translations to the streets database.
* Registering users are asked to create a username, provide an email address, state their skill level in Irish, state their location, and, optionally, to provide a short public biography.

#### User Accounts and Profile
* the details provided during registration by each user are presented on individual profile pages - of course, email addresses are kept private.
* all existing profiles can be **edited**. User accounts can be **deleted**.
* forgotten passwords can be reset through a link provided by an automated email communication.

#### Search Streets
All streets in the index can be searched by name on the home page. The select 'search' option whittles down the selection options as the user types. 

#### Street Pages
Each street page provides the street-name in English with the post code. If translations are available, they will be presented in card format beneath. If there are not yet any available translations, the user is given the opportunity to contribute one.

#### Translations
* Member Users can **add** translations, or **edit** and **delete** any of the translations they contribute. 
* A user can only add one translation per street.
* A user's translation can be their own, or if they're using a translation coined by someone else, they must enter details about their source.
* Users are asked to provide a note to explain or justify a translation.
* Each street can have multiple suggested translations, but they must come from different users.
* A list of translations provided by a user will appear on their profile page.
* A list of the five most recent translations added to the database will appear in a 'recent activity' sidebar on all pages, with some truncated details and a 'time ago' label.
* Users can click on any of the 'recent activity' cards to go straight to the street page, or to the profile page of the contributing user.
* Any translation activity requires logging in. Any users who are not logged in will receive a flash message explaining this.

### Testing
The application was tested manually by walking through the features from the perspective of the two targeted user groups: **Unregistered Users** who are looking for a translation, or who would like to browse the database or to register; and **Registered Users** who can add to or edit the database or delete their contributions. Registered users can also definitively delete their account, although the data they contributed in the form of translations will persist, unless they have been deleted before the account is shut down. Testing was also carried out on browser compatibility. 

The testing process is detailed [here](App/docs/testing.md).

### Features Left to Implement
- Map visualisation of streets. This was an original feature in the application design. However, the various APIs used to provide coordinates for streets were unable to find data for 700 of the 4000 streets. Since the feature couldn't be applied to all streets, and the number of streets with missing data was substantial, the feature was removed and will be added once the geolocation data can be obtained.
- User authentication
- User up-voting or down-voting of translations
- Reverse search order (Irish to English)

## Database Organisation
Sráideanna! uses a document-oriented database using MongoDB. The chosen structure was developed by progessing through the following steps:
- defining the principal collections within the database - users, streets and translations.
- refining the fields each user or translation document should contain.
- exploring the relationship between collections.
- developing the application's Python classes and route logic based on all these considerations.

Some documentation of this process as well as sample documents from the database itself can be found in the [database documentation](App/docs/db.md).

## Code

### Languages and tools used on the application include:

### Code
- **HTML**, **CSS**, **JavaScript**, and **Python**
  - Base languages used to create application
- [Flask 1.1.1](https://palletsprojects.com/p/flask/)
    - **Flask** is used as micro-framework to create and manage the application
- [MongoDB](https://www.mongodb.com/)
    - **PyMongo** is a MongoDB extension for Flask. 
- [Bootstrap 4.0.0](https://getbootstrap.com/)
    - **Bootstrap** (with JQuery) is used to render a responsive layout and most of the UI components of the application

### Deployment and Hosting

- [Heroku](https://www.heroku.com/)
    - The Cloud Application Platform **Heroku** hosts the Sráideanna application.
    - Deployment notes: Heroku CLI to push app to Heroku -- ensure Procfile created and set environment variables to Heroku config vars.
 
### Getting the code up and running

1. Create a virtual environment running Python3 (3.7.5).
2. Clone this repository by running the following command: ```git clone https://github.com/rumack/sraideanna.git```.
3. Install requirements using Pip: ```pip install -r requirements.txt```.
4. Set up a MongoDB database and connect the application to it.
5. Paste your MongoDB connection string into a MONGO_URI environment variable.
6. You will also need to add a SECRET_KEY environment variable to your local system
7. If you wish to test the password reset functionality, you will need to add MAIL_USER and MAIL_PASSWORD environment variables to your local system. The function is set to use Gmail smtp server, but this can be changed in the utils.py file.
8. Run the application from the application directory: ```python run.py```.
9. The application will now run on [localhost](http://127.0.0.1:5000).





Jump to [testing documentation](App/docs/testing.md).
Jump to [database documentation](App/docs/db.md).

