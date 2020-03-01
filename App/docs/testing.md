# Testing
The application was tested manually by walking through the features from the perspective of the two targeted user groups: **Unregistered Users** who are looking for a translation, or who would like to browse the database or to register; and **Registered Users** who can add to or edit the database. Testing was also carried out on browser compatibility. 

## Unregistered User Experience
The following was used to test the functionality of the application for unregistered users:

### Basic Navigation

#### i. on smaller screens click the hamburger menu 
- the navigation menu drops down to display the 'home', 'about', 'login', 'register' links.

#### ii. hover over navigation links
- the background color and font color change in response to hovering.

#### iii. click any of the 'about', 'login', 'register', 'home' or 'Sráideanna!' links in the main navigation
- the appropriate page is displayed and the appropriate link is highlighted.

#### iv. click any of the 'home', 'about', or 'register' links in the footer navigation
- the appropriate page is displayed.

#### v. click the GitHub logo in the footer.
- the GitHub repository for the Sraideanna! applcation opens in a new tab

#### vi. click the name of 'RoRo' in the bottom line of the footer
- the GitHub profile page for RoRo opens in a new tab.

### Street Search

##### i. click the **'find a street'** button to scroll down to street search; a login button is also visible:
- page scrolls to select input.

##### ii. enter the first few letters of a street to search:
- select options are refined according to input.

##### iii. once a street is selected, click **'select'** button:
- the street page opens with the name of the street in English and the post code. If there are translations, they are presented in card format beneath. Otherwise, a card encouraging the user to add a translation is displayed.

#### i. click on the username in a translation card
- the public profile associated with the username is displayed.

##### iv. click the **'add translation'** button:
- as this user is not logged in, they are redirected to the login page and a **flash message** appears: <em>"You must be logged in to visit this page."</em>.

### View profiles

#### i. the unregistered user visits the public profile of a registered user
- the profile presents the following: 
username 
location
skill level
avatar
translations total
translation cards

### Recent Activity Sidebar

#### i. click on the username in any of the 'recent activity' cards
- the public profile associated with the username is displayed.

#### ii. click on any of the Irish translations in a 'recent activity' card
- the appropriate street page is displayed.

### User Registration

##### i. click the **'register'** link:
- the register page opens and displays the registration form.

##### ii. submit a form after leaving a field blank (except the optional 'bio' field):
- form is not validated and a warnng appears below the field with the message: <em>This field is required</em>, or for the radio buttons: <em>Not a valid choice</em>.

##### iii. submit a form with a username less than 2 or more than 20 characters in length:
- form is not validated and a warnng appears below the 'username' field with the message: <em>Field must be between 2 and 20 characters long</em>.

##### iv. submit a form with an invalid email address:
- form is not validated and a warnng appears below the 'email' field with the message: <em>Invalid email address</em>.

##### v. submit a form when the 'password' and 'confirm password' fields do not match:
- form is not validated and a warnng appears below the 'confirm password' field with the message: <em>Your passwords must match</em>.

##### vi. submit a form when the username entered is already found on the database:
- form is not validated and a warnng appears below the 'username' field with the message: <em>Sorry, the username you chose is already taken. Please choose another</em>.

##### vii. submit a form when the email address entered is already found on the database:
- form is not validated and a warnng appears below the 'email' field with the message: <em>Sorry, an account already exists for that email address</em>.

##### viii. submit a form which validates with success:
- form is validated and the user is redirected to the login page. A **flash message** appears above the login form with the message: <em>Account created for <username>! You can now log in</em>.


## Registered User Experience
The following was used to test the functionality of the application for registered users who are logged in:

### Logging in

#### i. click on 'login' link and enter user email address and password
- user is now logged in and redirected to homepage. The username appears beside the 'logout' link in main navigaton bar.

#### ii. before logging in, go to any street page and click 'add translation' button. User is redirected to login page. Enter login details and click on 'login' button
- user is logged in but this time is not redirected to the home page, but to the add translation form the user tried to access before logging in. The application remembers their intended action just before login.

### Basic Navigation

#### i. on smaller screens click the hamburger menu 
- the navigation menu drops down to display the 'home', 'about', 'profile', 'logout' links.

#### ii. hover over navigation links
- the background color and font color change in response to hovering.

#### iii. click any of the 'about', 'profile', 'logout', or 'Sráideanna!' links in the main navigation
- the appropriate page is displayed and the appropriate link is highlighted.

#### iv. click any of the 'home', 'about', or 'register' links in the footer navigation
- the appropriate page is displayed - except for 'register': as the user is logged in and obviously already registered, the user is redirected to the home-page.

#### v. click the GitHub logo in the footer
- the GitHub repository for the Sraideanna! applcation opens in a new tab.

#### vi. click the name of 'RoRo' in the bottom line of the footer
- the GitHub profile page for RoRo opens in a new tab.

### Street Search

##### i. click the **'find a street'** button to scroll down to street search; a login button is not visible for logged in users:
- page scrolls to select input.

##### ii. enter the first few letters of a street to search:
- select options are refined according to input.

##### iii. once a street is selected, click **'select'** button:
- the street page opens with the name of the street in English and the post code. If there are translations, they are presented in card format beneath. Otherwise, a card encouraging the user to add a translation is displayed.

#### i. click on the username in a translation card
- the public profile associated with the username is displayed.

##### iv. click the **'add translation'** button:
- the 'add translation' form is displayed.

### View profiles

#### i. the registered user visits the public profile of another registered user
- the profile presents the following: 
username 
location
skill level
avatar
translations total
translation cards

#### ii. the registered (and logged in) user visits their own profile (either by clicking the 'profile' link in the main navigation, or by clicking on their username on a 'street' page or in the 'recent activity' sidebar)
- the profile presents the following: 
username 
location
personal email
skill level
avatar
an 'edit profile' button
translations total
translation cards

### Adding a translation

#### i. click on the 'add translation' button on any street page
- if current user has not already provided a translation for this street, the 'add translation' form is displayed.

#### ii. user clicks on the 'add translation' button on a street page where they have already provided translation
- the translation form doesn not open. Rather the user remains on the 'street' page and the following **flash message** is displayed: <em>Translations are limited to one translation per street per user</em>.

#### iii. user submits 'add translation' form without a translation
- an error message appears beneath the input field: <em>This field is required.</em>

#### iv. user submits 'add translation' form without a note
- an error message appears beneath the input field: <em>This field is required.</em>

#### v. in 'add translation' form, if the 'Myself' radio button is selected under the 'translation source' label
- the 'source details' input field is disabled

#### vi. in 'add translation' form, if the 'Other' radio button is selected under the 'translation source' label
- the 'source details' input field is enabled

#### vii. in a 'add translation' form, for a street where another user has already added a translation, if the current user enters the same translation and clicks to submit the form (i.e. if the translation is already found on the database)
- the form is not validated and the following **flash message** appears: <em>Sorry, the same translation has already been provided by another user.</em>

#### viii. an 'add translation' form is validated and sent
- the user is redirected to the relevant street page where the translation card has been added - complete with 'edit' and 'delete' buttons. The following **flash message** is also displayed: <em>Translation added successfully</em>.

### Editing a translation

#### i. user clicks on 'edit tanslation' button
- the edit translation form opens, prepopulated with the original data

#### ii. user submits 'edit translation' form without a translation
- an error message appears beneath the input field: <em>This field is required</em>.

#### iii. user submits 'edit translation' form without a note
- an error message appears beneath the input field: <em>This field is required</em>.

#### iv. in 'edit translation' form, if the 'Myself' radio button is selected under the 'translation source' label
- the 'source details' input field is disabled.

#### v. in 'edit translation' form, if the 'Other' radio button is selected under the 'translation source' label
- the 'source details' input field is enabled.

#### vi. an 'edit translation' form is validated and sent
- the user is redirected to the street page where the relevant translation card has been edited. The following **flash message** is also displayed: <em>Translation edited successfully</em>.

### Deleting a translation

#### i. on a 'street' page where the current user has already added a translation, the user clicks the delete button
- a 'confirm' dialogue is displayed with the question: <em>Are you sure you want to delete this translation?</em>. If user clicks 'OK', the page is updated and the translation is removed. The following **flash message** is displayed: <em>Your translation has been deleted</em>. If the user clicks 'cancel' in the confirm dialogue, the delete action is cancelled.

### Editing a profile

#### i. user clicks on 'edit profile' button on personal profile page
- the edit profile form is displayed, prepopulated with the original data.

#### ii. user edits profile and then clicks the 'Edit Profile' button
- The form is validated and the page redirects to the profile page. The following **flash message** is displayed: <em>You've successfully updated your profile</em>.

#### iii. user edits profile, including an **email address change**, and then clicks the 'Edit Profile' button
- The form is validated and the page redirects to the login page. The following **flash message** is displayed: <em>You've successfully updated your profile. Please log in again</em>. Since email addresses are used for login, the user is obliged to log in again.

### Deleting an account

TBC***********************************************

### Recent Activity Sidebar

#### i. user successfully adds translation
- the 'recent activity' sidebar is immediately updated to show addition, complete with 'time ago' timestamp. 

#### ii. user successfully edits translation
- the 'recent activity' sidebar is immediately updated to show edit, complete with 'time ago' timestamp. 

### Logging out

#### i. logged in user clicks the 'log out' button in navigation bar
- redirection to login page. Navbar changes to show that no user is logged in. 'Login' button is displayed beside 'Find a street' button in homepage header.



### Broswer compatibility 
The application was tested in each of the following browsers:
  - Google Chrome
  - Opera
  - Microsoft Edge
  - Mozilla Firefox
  - Safari
 
All of the browsers were compatible except **Opera** which displayed an occasional and inconsistent bug. On any of the profile pages (Pitcher/Catcher/Pitch), when the card was opened to reveal further details, the card element would 'shake' for a second before stopping. This also happened intermittently when selecting the dropdown menu.  