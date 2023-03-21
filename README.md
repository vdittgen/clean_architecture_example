# Clean Architecture and CQRS (command query responsibility segregation) with Python3, FastAPI and Flask.
This project is a simple example of how to use the clean architecture principles in a Python application.
API is using FastAPI while web app is using Flask.


# Folder Structure
The project uses a folder structure that is based on the clean architecture principles. The structure is as follows:

```
api/
|-- controller.py
|-- Dockerfile
|-- settings.py
|-- requirements.txt
web/
|-- controller.py
|-- Dockerfile
|-- templates/
|   |-- base.html
|   |-- index.html
|-- views.py
|-- settings.py
|-- requirements.txt
app/
|-- domain/
|   |-- user.py
|-- repositories/
|   |-- user_repository.py
|-- services/
|   |-- email.py
|-- use_cases/
|   |-- command/
|       |-- register_user.py
|   |-- query
|       |-- get_user.py
|-- adapters/
|   |-- command_handlers.py
```

The **app/** directory is the top-level directory for the application. It contains the main application code, configuration files, and other resources.

The **domain/** directory contains the domain entities and value objects for the application. These are the core concepts and data structures that define the business logic of the application.

The **repositories/** directory contains the interfaces and implementations for the application's data access layer. These are responsible for persisting and retrieving domain entities and value objects.

The **services/** directory contains the interfaces and implementations for any external services that the application depends on, such as email services or payment gateways.

The **use_cases/** directory contains the use cases for the application. These are the high-level business rules and workflows that orchestrate interactions between the domain entities, repositories, and services. We also included subdirectories to include the CQRS (command query responsibility segregation) pattern.

The **adapters/** directory contains the adapters for the application. These are the lower-level components that handle external input and output, such as command-line interfaces or web APIs.


# Clean Architecture
The folder structure of the project is based on the **clean architecture principles** and **CQRS (command query responsibility segregation)**, which are designed to promote **modularity, testability, and maintainability** in software applications. The main idea behind clean architecture is to separate the application logic into different layers or components, each with its own well-defined responsibilities and interfaces.

The clean architecture principles can be seen in our project structure in a few different ways:

The separation of the domain entities, repositories, services, use cases, and adapters into separate directories promotes modularity and separation of concerns.

The use of interfaces for the repositories, services, and adapters allows for easy swapping and mocking of these components during testing and development.

The high-level use cases define the business logic of the application in a way that is independent of any particular implementation details, such as the choice of database or web framework.

The web-specific adapters, such as Flask views and templates, are kept separate from the rest of the application logic, making it easy to replace or modify the web interface without affecting the underlying business logic.

By using the clean architecture principles, we can create applications that are easy to understand, maintain, and extend over time. The separation of concerns between different layers of the application makes it easy to test and modify individual components without affecting the rest of the application, and the use of interfaces allows for easy swapping and mocking of components during development and testing.

In our example project, we've used the clean architecture principles to create a simple user registration and activation workflow. We've separated the domain entities, repositories, services, and use cases into separate components, and used interfaces to define the interactions between these components. We've also included a web-specific adapter using Flask to handle incoming requests and serve dynamic HTML pages.

Overall, our project demonstrates how the clean architecture principles can be applied in a Python application to create a flexible, testable, and maintainable codebase.


# Start the API locally
```
make start.api
```

# Start the Web application locally
```
make start.web
```

# Start both API and Web app on a container
```
make start.docker
```

# Make a request to the API
```
curl -X POST http://localhost:8000/users -H 'Content-Type: application/json' -d '{"username":"vinicius","email":"john@gmail.com","password":"123","role":"DE"}'
```

```
curl -X POST http://localhost:8000/users/get -H 'Content-Type: application/json' -d '{"email":"john@gmail.com"}'
```
