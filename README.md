# VsBuy

VsBuy is a web application that compares for you and gives you the cheapest price of the most famous stores.

### Requirements 📋

* docker
* docker-compose

### Instalation 🔧

1. Clone this project.

2. Change of directory to the root of the project.
  cd vsbuy_backend

3. Build the images.
  docker-compose -f production.yml build

4. Run the migrations to create the tables in the database.
   docker-compose -f production.yml run --rm django python manage.py makemigrations
   docker-compose -f production.yml run --rm django python manage.py migrate

5. Run it in production
  docker-compose -f production.yml up -d

## Debugging ⚙️

1. In the root of project.
    docker-compose -f local.yml build

2. After construction run the containers.
    docker-compose -f local.yml up

3. If you want run the migrations.
   docker-compose -f local.yml run --rm django python manage.py makemigrations
   docker-compose -f local.yml run --rm django python manage.py migrate

## Built with 🛠️

* Django (django, django-celery-beat, django-redis, django-mailgun)
* Django REST FRAMEWORK
* Postgres

## Contributors ✒️

* **Daniel Silva** - *Backend * 
* **Edward Toledo** - *DataScientist* 

## License 📄

This project is licensed under The MIT License (MIT) - see the [LICENSE.md] (LICENSE.md) file for details

## Acknowledgment 🎁

* To Coach Ana Belisa Martinez.
* To Platzi Staff.
