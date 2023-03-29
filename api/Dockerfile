FROM arm64v8/python:3.10

ARG ENVIRONMENT=${ENVIRONMENT}
ENV ENVIRONMENT=$ENVIRONMENT

COPY . ${APP_ROOT}

RUN  pip3 install -r ${APP_ROOT}/requirements.txt
RUN apt-get update && apt-get install -y sqlite3
RUN sqlite3 example.db

EXPOSE 8000

ENV UVICORN_BIND=0.0.0.0:8000
CMD ["uvicorn", "controller:api_app", "--host", "0.0.0.0", "--port", "8000"]