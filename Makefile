start:
	uvicorn app.adapters.api.controller:app --reload

start.docker:
	chmod 700 bash/docker.sh
	./bash/docker.sh

stop.docker:
	docker stop $(docker ps -q)