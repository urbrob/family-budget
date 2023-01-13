BASE_DIR := .

start-app:
	docker-compose up

build-app:
	docker-compose build

migrate:
	docker-compose exec -T web python manage.py migrate

gen-migration:
	docker-compose exec -T web python manage.py makemigrations

test:
	docker-compose exec -T web python manage.py test budgets

reformat-backend:
	docker-compose exec -T web python -m black ./
