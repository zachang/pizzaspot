# Pizzaspot
A concept for pizza ordering app

[![Build Status](https://travis-ci.org/zachang/pizzaspot.svg?branch=develop)](https://travis-ci.org/zachang/pizzaspot)
[![Coverage Status](https://coveralls.io/repos/github/zachang/pizzaspot/badge.svg?branch=develop)](https://coveralls.io/github/zachang/pizzaspot?branch=develop)


## Docker Project Setup

- Clone the repo.
- Have at least Python 3.6.x installed. 3.8 was used.
- Open project with your favorite editor
- Create a .env file in your root directory as described in .env.example file.
- Run `docker-compose build`
- Changes to Dockerfile will need re-building.
- After build, Run `docker-compose up api` to start app
- For Test, Run `docker-compose run --rm api pipenv run python manage.py test`

    ## Migarations
    
    - Run `docker-compose run --rm api pipenv run python manage.py makemigrations`
    - Run `docker-compose run --rm api pipenv run python manage.py makemigrate`
    - For new model changes run `1st` step before `2nd` step.

## Setup without Docker
- Clone the repo.
- Have at least Python 3.6.x installed. 3.8 was used.
- Have pipenv installed in your device; [pipenv](https://pypi.org/project/pipenv/)
- Open project with your favorite editor
- Create a .env file in your root directory as described in .env.example file.
- Run `pipenv shell` (creates virtual environment)
- Run `pipenv install` (installs all dependencies)
- Run `pipenv run python manage.py runserver`
- For test, Run `pipenv run python manage.py test`
    ## Migarations
    
    - Run `pipenv run python manage.py makemigrations`
    - Run `pipenv run python manage.py migrate`
    - For new model changes run `1st` step before `2nd` step.


## Technologies Used

- [Django](https://www.djangoproject.com/) - Python web framework used
- [Django rest framework](https://www.django-rest-framework.org/) - Used for rapidly building RESTful APIs based on Django models.
- [Postgres](https://www.postgresql.org/) - Object-relational database used

## How To Contribute

- Fork this repository to your GitHub account
- Create your feature branch
- Commit your changes
- Push to the remote branch
- Open a Pull Request

## API Documentation

- [Pizzaspot Doc](https://documenter.getpostman.com/view/7627295/TVYPztLF)

## Author

- Dawuda Ebenezer Zachang