FROM arm64v8/python:3.10

ARG ENVIRONMENT=${ENVIRONMENT}
ENV ENVIRONMENT=$ENVIRONMENT

COPY . ${APP_ROOT}

RUN  pip3 install -r ${APP_ROOT}/requirements.txt

EXPOSE 8000

ENV UVICORN_BIND=0.0.0.0:8000
CMD ["uvicorn", "controller:api_app", "--host", "0.0.0.0", "--port", "8000"]