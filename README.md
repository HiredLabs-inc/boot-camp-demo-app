# Hired Labs, Inc. Coding Boot Camp Example App

This is a simple "todo list" web application that is built during a 6-week course
on basic web development using Django (Python).

It has three pages to demonstrate page navigation, and the main web app
demonstrates the basic CRUD operations.

The intent of this project is for people to understand the basic mechanics of a
web application, and use this as a template to build something more interesting.

The installation directions are for running the app and website directly in
[PythonAnywhere](https://www.pythonanywhere.com/), but it can easily be run
locally.


## Installation

### 1. Installation steps

### Linux/MacOS
#### 1.1. Clone the repository


#### 1.2. Create a .env file
Set a DJANGO_SECRET_KEY variable to any string of random characters.

#### 1.3 Configure PythonAnywhere
Navigate the "Web" section of your PythonAnywhere account.

##### 1.3.1 Create an App
Choose the latest version of Python, and "manual configuration" for the framework.


##### 1.3.2 Configure wsgi.py
Under "Code" in the "Web" section of PythonAnywhere click the link to open the
wsgi.py file, comment out the pure wsgi app, and uncomment the Django app.

Save and close the wsgi.py file.

##### 1.3.3 Set paths

Under "Code" in the "Web" section of PythonAnywhere add the path
"/home/username/mysite" to both the source code and the working directories.

Change the "username" to your username.

Under "Static files" further down the page in the "Web" section, set the
url to "/static/" and the path to "/home/username/mysite/static_main/".

Optionally turn on the "Force HTTPS" toggle towards the bottom of the page.

#### 1.4. Reload and Refresh
Reload the source code on your PythonAnywhere server by clicking the big, green
button towards the top of the "Web" section.

Refresh your browser, or navigate to your web app by visiting
"https://username.pythonanywhere.com/", replacing "username" with your username.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss the change. Please see
CODE_OF_CONDUCT.md for details on our code of conduct.

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](code_of_conduct.md)
## License
[GPL-3.0 license](https://www.gnu.org/licenses/gpl-3.0.en.html)
