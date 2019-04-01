[![Build Status](https://travis-ci.org/Losiek86/project5.svg?branch=master)](https://travis-ci.org/Losiek86/project5)


[Dog sanctuary with ecommerce (code institute project 5)](https://e-commerce-mini.herokuapp.com/)
=========================================================

This Django project is a combined online shop and Dogs sanctuary with possibility of adding pupils, articles by administration and comments to articles, applying to become a volontary by users, where admins have options to show the process of aplication.

The key features of the app are:

* Users can check the shop with rpoducts offered
* Users can 'Order' a product of their choosing
* Users can apply for becoming volunteer online.
* Users can add comments to articles
* Staff can add articles
* Staff can add new products to shop
* Staff can add new options in donation page althought after submiting donation by User its goin to under development page
* Staff can add new pupils to the page via the administration panel

This project was developed as the final project in a diploma in Full Stack Software Development through The Code Institute.

The running site can be accessed here https://e-commerce-mini.herokuapp.com/

UX
----
The app was developed to be used by any pet sanctuary to help them getting funds not only by donations but by selling product by them.

__User Stories__

User stories were developed to plan out the features for the application.

__Site Visitor User Story__

* As a site visitor I should see the shopping site with products as well as the donation site.
* As a site visitor I should be able to add products to a shopping cart.
* As a site visitor I should be able to view the contents of the shopping cart
* As a site visitor I must be able log in or register to make an order

__Registered User User Story__

* As a registered user I should be able to place an order.
* As a registered user I should be able to pay in a secure and confidential manor.
* As a registered user I should be able to view profile page
* As a registered user I should be able to make comment for articles
* As a registered user I should be provided of change of status of my application for volunteer.

__Staff User Story__

* As staff I should be able to add ne products to the shopping page.
* As staff I should be able to full database by the administration panel.
* As staff I should be able to add new donation options
* As staff I should be able to mark applications as 'received' when ill see new application.
* As staff I should be able to change application status.
* As staff I should be able to add new pupils to the site

__Admin User Story__

* As admin I should have all Staff privileges


Features
---------

__Existing Features__

* Display main page and all others
* User registration
* Customer can order products
* Customer can apply to be volunteer by 'Portal' view.
* Customer can view all the products in shop
* Customer can add new comments to articles
* Staff can upload new products/ donations/ pupils to the site
* Staff can upload new articles to the site


__Future Features__

* As admin I should be able to backup the database as .csv file.
* Develop donations page
* Develope further dogs adoption page


Technologies Used
-----------------------
* __VirtualEnvironment__ (https://docs.python.org/3/library/venv.html) was used to wrap the project.
* __Git__ (https://git-scm.com/) was used for version control.
* __GitHub__ (https://github.com/) was used to share the repository.
* __Heroku__ (https://dashboard.heroku.com/) was used to host the application.
* __Python3.6__ (https://docs.python.org/3/) was used to develop all back-end code.
* __Django-1.11.18 (https://www.djangoproject.com/) web development framework was utilised for efficient app development.
* __HTML5__ (https://www.w3.org/TR/html5/) was used to develop front-end templates.
* __CSS__ (https://www.w3.org/Style/CSS/) was used for styling of front-end templates.
* __Bootstrap 3.3.7__ (https://stackpath.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css) was used for more effective CSS layout styling.
* __Font-Awesome 5.3.1__ (https://use.fontawesome.com/releases/v5.3.1/css/all.css) was for the icons were used for user familier icons.
* __Google Fonts __ (https://fonts.google.com/) were used for the nav bar text and the home page quote.
* __Stripe__ (https://www.stripe.com) was used for secure credit card payments
* __Pillow__(https://pypi.org/project/Pillow/) Python Imaging Library used for interpreting images
* __PostgresSQL__(https://www.postgresql.org/) open source object-relational database was used for storing data

Testing
-----------------------


* Open the site and sign in/ sign out
* In a seperate browser register a new account using your email address
* Add a comment to article
* Apply to be volunteer
* Check articles and pupils more specificaly



__Code Validation__

* __Python__ was validated using http://pep8online.com/.
* __HTML__ was validated using https://validator.w3.org/. Due to the Django template code embedded in the HTML there were a number of errors.
* __CSS__ was validated using https://jigsaw.w3.org/css-validator/.

__Continuous Integration__

Travis CI 

__Automated Testing__

__Visual Testing__



|                                                       | Galaxy S5 | Galaxy S7      | Pixel 2 | Pixel 2XL | iPhone 5/SE | iPhone 6/7/8 | iPhone 6/7/8 + | iPhone X | iPad  | iPad Pro   | Responsive 1366 x 768 | Responsive 1680 x 1050 |  
| ----------------------------------------------------- | --------- | -------------- | ------- | --------- | ----------- | ------------ | -------------- | -------- | ------| ---------- | --------------------- | ---------------------- |
| Home                                                  | OK        | OK             | OK      | OK        | OK          | OK           | OK             | OK       | OK    | OK         | OK                    | OK                     |
| Shop                                                  | OK        | OK             | OK      | OK        | OK          | OK           | OK             | OK       | OK    | OK         | OK                    | OK                     |
| Nav                                                   | OK        | OK             | OK      | OK        | OK          | OK           | OK             | OK       | OK    | OK         | OK                    | OK                     |
| Donate                                                | OK        | OK             | OK      | OK        | OK          | OK           | OK             | OK       | OK    | OK         | OK                    | OK                     |
| Log in/ Register                                      | OK        | OK             | OK      | OK        | OK          | OK           | OK             | OK       | OK    | OK         | OK                    | OK                     |
| Cart                                                  | OK        | OK             | OK      | OK        | OK          | OK           | OK             | OK       | OK    | OK         | OK                    | OK                     |
| Checkout                                              | OK        | OK             | OK      | OK        | OK          | OK           | OK             | OK       | OK    | OK         | OK                    | OK                     |
| Profile                                               | OK        | OK             | OK      | OK        | OK          | OK           | OK             | OK       | OK    | OK         | OK                    | OK                     |
| Articles                                              | OK        | OK             | OK      | OK        | OK          | OK           | OK             | OK       | OK    | OK         | OK                    | OK                     |
| Article                                               | OK        | OK             | OK      | OK        | OK          | OK           | OK             | OK       | OK    | OK         | OK                    | OK                     |
| Pupils                                                | OK        | OK             | OK      | OK        | OK          | OK           | OK             | OK       | OK    | OK         | OK                    | OK                     |
| Pupil                                                 | OK        | OK             | OK      | OK        | OK          | OK           | OK             | OK       | OK    | OK         | OK                    | OK                     |
| add comment / apply                                   | OK        | OK             | OK      | OK        | OK          | OK           | OK             | OK       | OK    | OK         | OK                    | OK                     |


Development
------------------------

The purpose of the project was to allow pet sanctuaries to be able not only to collect donations but to sell products.

Also it is a perfect place to wrote article for Your users, get comments from them, look for a volunteers to help you as well as to show The pupils you are taking care off, and in future organize an adoptions for them through the site

Deployment
------------------------

__Requirements__

The system hosting the app must have a number of python packages installed.
A full list can be found at requirements.txt
__System Variables__

The following system variables must be set in the host environment.

* STRIPE_PUBLISHABLE, publishable key assigned to you when you register an account with Stripe https://stripe.com/ie
* STRIPE_SECRET, secret key assigned to you when you register an account with Stripe https://stripe.com/ie
* SECRET_KEY, generated by django when you start a new app. See setttings.py file
* DATABASE_URL, generated when you set up a PostGres database, i.e. when using 'Heroku Postgres' add-on under resources when deploying app on Heroku.

__Deployed vs Development__

__gitignore__

A number of files and folders in the local development environment were not deployed with the project. These files and folders were included in a .gitignore file.

All system variables were declared in an env.py file. As many of these variables were passwords this was omited from git repo from the initial git.


Credits
------------

__Content__

Most of the site contains standard lorem ipsum text.

__Media__

All the images were taken from a [Pixabay.com](https://pixabay.com/)


Running App
------------------------


https://e-commerce-mini.herokuapp.com/


