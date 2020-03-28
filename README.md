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
- source env/bin/activate

The first time you will need export environments to run locally:
- export APP_SETTINGS="config.DevelopmentConfig"
- export DATABASE_URL="postgresql://postgres:postgres@localhost:5432/rental_shop"

After that, execute:
- pip install -r requirements.txt
- python manage.py db init
- python manage.py db migrate
- python manage.py db upgrade

Finally, execute application:
- flask run