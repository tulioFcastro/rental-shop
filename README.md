# Python

- sudo apt-get update
- sudo apt-get install python3.6

# Database - PostgreSQL

## Install
sudo apt-get install postgresql postgresql-contrib

## PostgreSQL cli
- sudo -i -u postgres
- psql
- create role rental_shop;
- drop database rental_shop;
- create database rental_shop;
- grant all privileges on database rental_shop to rental_shop;

# Run Application
- virtualenv --python=python3 env --no-site-packages
- source env/bin/activate

The first time you will need export environments to run locally:
- source script.sh

After that, execute:
- pip install -r requirements.txt
- python manage.py db init && python manage.py db migrate && python manage.py db upgrade

Finally, execute application:
- flask run