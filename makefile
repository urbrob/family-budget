BASE_DIR := family_budget

start-app:
	python $(BASE_DIR)\manage.py runserver

migrate:
	python $(BASE_DIR)\manage.py migrate


gen-migration:
	python $(BASE_DIR)\manage.py makemigrations
