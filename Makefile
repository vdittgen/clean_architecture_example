start.api:
	uvicorn api.controller:api_app --reload

start.web:
	gunicorn "web.controller:web_app"

start.docker:
	docker-compose up

start.docker.build:
	docker-compose up --build

stop.docker:
	docker-compose down