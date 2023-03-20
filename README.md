# clean_architecture_example
Example of an web application and API wrote in Python3, API is using FastAPI while web app is using Flask. The objective is to explore Clean Architecture concepts.

# Start the app localy
```
make start
```

# Start the app on a container
```
make start.docker
```

# Make a request to the container
```
curl -X POST http://localhost:8000/users -H 'Content-Type: application/json' -d '{"username":"vinicius","email":"john@gmail.com","password":"123","role":"DE"}'
```

```
curl -X POST http://localhost:8000/users/get -H 'Content-Type: application/json' -d '{"email":"john@gmail.com"}'
```
