# django-basics

## About
Following video series from chaiaurcode: https://www.youtube.com/watch?v=CLDDcXV4H50&list=PLu71SKxNbfoDOf-6vAcKmazT92uLnWAgy
- Using `uv` for package management: https://pypi.org/project/uv/
    - use `uv pip install xyz`

## Local running
- Install `uv`
- `uv venv`

## Notes
- `django-admin` is a cli that comes with django itself
    - `django-admin startproject <name>`: create a new project with a given name
    - `python manage.py runserver` -> run the local development server, optionally supply a port number. Also creates a sqlite db file.
- `manage.py`: entrypoint file for the server, controls settings, env variables
- `db.sqlite3`: Database file. Project is easily customizable to move from sqlite to postgres or other relational dbs
- Nomenclature: need to know where to create files:
    1. Root level: where manage.py is
    2. Project level: inside the chaiaurDjango/chaiaurDjango folder
    3. App level: Folders within the project
- `chaiaurDjango/`
    - `settings.py`: specify all project-level settings: apps, variables, templates, database settings, time zone, etc
    - `urls.py`: add routing for all files here. comes with admin by default
    - `views.py`: controllers, i.e business logic
    - `model.py`: all database models
- Overall flow: Request comes in -> urls.py tells the program which function to route to -> function in views.py performs the computation and returns required data -> models.py is used to interact with database if needed
