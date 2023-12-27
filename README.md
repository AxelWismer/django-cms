# Django-CMS
Content managment system in Django to manage data in pre-existing databases

### Log in page 
Sing in the applications with this test credentials:

    user: admin
    password: admin

![alt text](/docs/login.png)

### Dashboard
The dashboard is the main page of Django CMS. It provides an overview of all your content and allows you to navigate through it easily.

![alt text](/docs/dashboard.png)

### List View
This is a paginated view. It allows you to search records using filters and a search bar.

You can set the fields you see in this list.

![alt text](/docs/list_view.png)

### CRUD Form
Single form for creating updating and deleting records

![alt text](/docs/CRUD_form.png)

## Docs

### Models
This tool allows creating visual representations of the database

![alt text](/docs/models.png)
#### Generating the docs
    python manage.py graph_models -o docs/models.png

## Development

### Download the repository
### Install python 3.9 (for linux)
    sudo apt update
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt install python3.9
    sudo apt install python3.9-venv

### Create virtual environment
    python -m venv venv

### Install libraries:
    pip install -r requirements.txt
### Uninstall all Packages
    pip freeze | xargs pip uninstall -y


## Deploy Django App as AWS Lambda
### Configure AWS Profile
    aws configure
Then enter the new credentials
### Collect the static files and place them in the S3.
    python manage.py collectstatic

### Deploy lambda with Zappa
    zappa init
    zappa deploy
    zappa update

### Database
This example uses a SQLite DB as a file "db.sqilte3". This file has been uploaded in GitHub to be able to try the application.

