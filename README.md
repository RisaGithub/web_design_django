# web_design_django

## Start project
### install venv
```
python -m venv venv
```
### activate venv
```
venv/Scripts/activate
```
### upgrade pip
```
venv\Scripts\python.exe -m pip install --upgrade pip
```
### install requirements
```
pip install -r  requirements.txt
```

## Run server
```
cd website
```
```
python manage.py migrate
```
```
python manage.py runserver
```

## Create superuser
```
python manage.py createsuperuser
```

## Start an app
### Run this command:
```
python manage.py startapp <app_name>
```
### Add app config to INSTALLED_APPS in settings.py:
```
INSTALLED_APPS = [
    ...
    '<app_name>.apps.<App_name>Config',
    ...
]
```
