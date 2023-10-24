lint:
	poetry run flake8 remotejobs --exclude=migrations,config/settings.py

test:
	poetry run python manage.py test