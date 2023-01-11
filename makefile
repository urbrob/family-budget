BASE_DIR := .

start-app:
	docker-compose up

build-app:
	docker-compose build

migrate:
	docker-compose exec -T web python app/manage.py migrate

gen-migration:
	docker-compose exec -T web python app/manage.py makemigrations
