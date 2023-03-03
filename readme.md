## Prerequisite

- Python 3.11
- Rdbms mysql/postgresql(Postgresql recomended)

## Set Up Database

- create database with name `django_todo`

## How to Install

- create virtual environtment(Linux/macOS, Linux recomended)

```bash
python -m venv env
```

- sign in virtualenv

```bash
source env/bin/activate
```

- install all dependencies

```bash
pip install -r requirements.txt
```

- migration database

```bash
python manage.py makemigrations
python manage.py migrate
```

- run the server

```bash
python manage.py runserver
```
