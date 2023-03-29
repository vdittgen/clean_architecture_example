start.api:
	sqlite3 example.db &
	uvicorn api.controller:api_app --reload

start.web:
	sqlite3 example.db &
	gunicorn "web.controller:web_app"

start.docker:
	docker-compose up

start.docker.build:
	docker-compose up --build

stop.docker:
	docker-compose down