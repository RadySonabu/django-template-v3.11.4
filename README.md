# Django template for v3.11.4

This is my django project and the goal is to easily start a project with common functionalities like authentication, authorization, registration, and etc. Also deploy it as easy as possible.

UPDATE: zappa does not support python 3.11 yet. So I will use python 3.10 env

I'm currently using [readme.so](https://readme.so/) to create this README.md file.

deployed here: https://gcxw2bzlyg.execute-api.ap-southeast-1.amazonaws.com/dev

TODO:
BOTH Django & DjangoRestFramework
##Authentication & Authorization

- Login/Logout
- Retrieve/Update the Django User model
- Password change
- Password reset via e-mail
- Social Media authentication

Major Packages used

- Django
- django-corsheaders
- django-allauth
- djangorestframework
- django-crispyforms
- django-debug-toolbar
- boto3 & botocore
- whitenoise
- zappa
