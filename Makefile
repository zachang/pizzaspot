migrate:
	pipenv run python manage.py migrate

migrations:
	pipenv run python manage.py makemigrations

pip-install:
	pipenv install

start:
	pipenv run python manage.py runserver

test:
	pipenv run python manage.py test

test_coverage:
	coverage run --source='.' manage.py test
	coverage report
	coverage html
