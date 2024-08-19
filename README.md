# backend
references
- https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page
- https://medium.com/@devsumitg/how-to-connect-reactjs-django-framework-c5ba268cb8be
- https://medium.com/@samradnus2001/how-to-secure-your-react-and-django-web-application-from-common-attack-cd6f31db0cf8
- https://blog.stackademic.com/django-react-secure-authentication-using-http-only-cookie-ac718f0a2797

# Setup

## On Windows

### Create a Virtual Environment 

#### Make sure u r in SMILE-NITK-WEBSITE folder
```
- python -m venv venv
```
### Activate the Virtual Environment 
```
- venv\Scripts\activate
```
### Installing the requirements for the project
```
- pip install -r requirements.txt
```
### Making migrations and running the server

#### Make sure u r in smile_backend folder
```
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver
```
## On macOS/Linux

### Create a Virtual Environment 

#### Make sure u r in SMILE-NITK-WEBSITE folder
```
- python3 -m venv venv
```

### Activate the Virtual Environment 

```
- source .venv/bin/activate
```

### Installing the requirements for the project
```
- pip install -r requirements.txt
```
### Making migrations and running the server

#### Make sure u r in smile_backend folder
```
- python3 manage.py makemigrations
- python3 manage.py migrate
- python manage.py createsuperuser
- python3 manage.py runserver
```

## For making requirements.txt after adding new packages
```
- python3 -m pip freeze > requirements.txt
```
## Additional Links

- https://www.prokerala.com/astrology/panchang/2024-april-09.html?loc=1263780





## Contents for .gitignore
#### Before pushing add a .gitignore file
#### Make sure the file is in SMILE-NITK-WEBSITE folder

```
# Ignore virtual environment
.venv/

# Ignore database file

# Ignore static files directory
staticfiles/

# Ignore media files directory
media/

# Ignore IDE or editor specific files
.vscode/
.idea/

# Ignore compiled Python files
*.pyc

# Ignore environment-specific settings file (if you have one)
.env

# Ignore local development settings (if you have one)
local_settings.py

# Ignore any other files or directories you don't want to include in version control
.gitignore

```