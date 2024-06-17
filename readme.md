# process

- python -m venv venv
- . .\venv\Scripts\Activate
- pip install django
- pip list
- pip freeze > requirements.txt
- **Inastal a DJANGO project ->** django-admin startproject sports_project .
- run server -> python manage.py runserver
- folder structure
  - settings.py -> settings of application
  - urls.py ->  path
- **Inastal a DJANGO app ->**django-admin startapp registration_app

## register application

- in project -> settings -> INSTALLED_APPS -> add name of application E.G registration_app

## run project

- start Project:
```py project_name.py runserver```
```python manage.py makemigrations```
```python manage.py migrate```

- add urls.py to apps folder
  - import views.py from app directory
- modify views.py in apps folder
- modify urls.py in project folder
- add models.py in app folder
- add forms.py in app folder

## set up URLs

- creat URLS.py in app folder
- import include, path
- Add a URL to urlpatterns as shown in example
  - e.g. url for app, inside Project folder
  - path('', include('registration_app.urls')),
- this URL will be for the APP

## creeate templates

- create templates folder in app folder
- create auth app
  - inside create partials folder -> HTML that not a full page
  - e.g. header and footer

## create forms

- in app folder create forms.py

## create views

- in app folder create views
- import forms

## URL

- import url for registration page
- import from.views

## Make migrations

- ```python manage.py makemigrations```
- ```python manage.py migrate```
- create super user
- ```python manage.py createsuperuser```
- start Project:
```py manage.py runserver```

## permisions

- We can set a permission for a specific table and only allow a user with the correct permissions to access or change the table.
- Django has a built-in permissions system we can make use of.
- We can use permission with our models to limit access to the data within that model’s database table
- limit access to what users can do

## Data Security

- We use ideas such as encryption and hashing to protect the data we store
- encryption = algorithm that we run our data through
  - we can then run a decrytion algorithm to get a get a key

## custom Permissions

- we can create our own permissions as well

```py
# import model we would like to create permison vfor 
from myapp.models import BlogPost
# import permisipn model 
from django.contrib.auth.models import Permission
# import content type
from django.contrib.contenttypes.models import ContentType
# get content type for model 
content_type = ContentType.objects.get_for_model(BlogPost)
# create a new permision obhject and store it
permission = Permission.objects.create(
  # codename = name it will use
  codename="can_publish",
  # name = overview of what its allowing user to do 
  name="Can Publish Posts",
  # content type
  content_type=content_type,
)
```

- get specific permission
- To add specific permissions to a user we first have to get
the permissions

```py
content_type = ContentType.objects.get_for_model(BlogPost)
permission = Permission.objects.get(
  codename="can_publish",
  content_type=content_type,
)

user.user_permissions.add(permission)
# check if user has correct permissions 
user.has_perm("myapp.change_blogpost")
```

- restrict users from accessing certain views

```py
from django.contrib.auth.decorators import permission_required
@permission_required("polls.add_choice")
def my_view(request):
```

## create super user

- python manage.py createsuperuser
- create group in admin site
- 