# Database - PostgreSQL

## Install
- sudo apt-get install postgresql postgresql-contrib

## PostgreSQL cli
- sudo -i -u postgres
- psql
- create role rental_shop;
- create database rental_shop;
- grant all privileges on database rental_shop to rental_shop;

# Run Application
- virtualenv --python=python3.7 env --no-site-packages
- source env/bin/activate

The first time you will need export environments to run locally:
- source script.sh

After that, execute:
- pip install -r requirements.txt

Finally, execute application:
- flask run


# Client side

The front-end was developed with the VueJS Framework and is inserted in the ```client``` folder.

### Project setup
- cd client
- npm install

### Compiles and hot-reloads for development
- npm run serve:development
