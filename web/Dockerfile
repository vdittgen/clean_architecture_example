FROM arm64v8/python:3.10

ARG ENVIRONMENT=${ENVIRONMENT}
ENV ENVIRONMENT=$ENVIRONMENT

COPY . ${APP_ROOT}

RUN  pip3 install -r ${APP_ROOT}/requirements.txt
RUN apt-get update && apt-get install -y sqlite3
RUN sqlite3 example.db

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8080", "controller:web_app"]
