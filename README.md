Starting the project


If you are using window then first of all

1. create virtual environment
```python -m venv venv```
2. Then activate that environment
```venv\Scripts\activate```
3. Then install Django in that environment
```pip install django```
4. Then create django project named mysite
```django-admin startproject mysite```


Run Server
```python manage.py runserver```


Create another app within your project

```python manage.py startapp blog```


Adding application
Adding Class BlogConfig to the INSTALLED APPLICATIONS list inder projects/settings.py

```python
INSTALLED_APPS = [
    'blog.apps.BlogConfig',
```


# Creating Admin User

```python manage.py createsuperuser```

error provided in cmd line
``` django.db.utils.OperationalError: no such table: auth_user ```

Will initially error. We need to create database first. 

## Create database and admin user

```python manage.py makemigrations```

Tells use ```No changes detected```
If we created db or models then we would see changes. The command makemigrations detects changes and prepares django to update the database. Then we will run:

```python manage.py migrate```

auth_user table should now exits. Running ```python manage.py createsuperuser``` should now work. 
Created Admin User
Username (leave blank to use 'prest'): Admin
Email address: admin@test.com
Password: test123

Now we can run the server again and attempt to log in as an admin. 


# Working with ORM (Object Relational Mapper)
ORM allows us to access our DB in a easy way

SQLite for development and PostGres for Production

Will create classes in Models.py file

after changes are made, I need to runt he makemigrations command again
```c
Migrations for 'blog':
  blog\migrations\0001_initial.py
    - Create model Post

```

makemigration command created file 
```\blog\migrations\0001_initial.py```

python manage.py shell to query the database using python
Need to import db
from blog.models import Post
from django.contrib.auth.models import User



# To View your Posts

Register your models in the blog/Admin.py file


# Adding forms

Best option would probably be to create a new app inside the Django project for Users   

```django_project>python manage.py startapp users```


# Crispy Forms

Installed using pip django-crispy-forms

1. Then open up settings.py to add to INSTALLED APPS
2. Added bootstrap4 at bottom of settings to CRISPY_TEMPLATE_PACK
3. Added {% load crispy_forms_tags %} to top of register.html page to use it
4. Updated forms.as_p to form|crispy to allow Bootstrap to take care of formating. 


# Setting up authentication system

Added conditional in the views html for logged in vs logged out. 

added Login redirect 
added decorator in Views.py for the profile to add security


# Adding Profile

Created profile for each user with one to one field

Added class Profile in Users/models file
then run python manage.py makemigrations
Then migrate
Then register in Admin.py

# Change storage location of profile pics

Update settings.py 

Set attrs 

```python
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

Serving files uploaded by a user during development¶
https://docs.djangoproject.com/en/4.0/howto/static-files/

**This is not suitable for production use!**


# Create profile whenever a User is created
Create Signals.py and import post_save
Update apps.py with ready function


## Adding pillow for pic resizing
