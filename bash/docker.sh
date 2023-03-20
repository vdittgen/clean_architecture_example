#! /bin/bash
docker build -t clean_app . && docker run --env ENV=dev --env LOG_LEVEL=DEBUG  -p 8000:8000 -it --rm --name clean_app clean_app
#--platform=linux/x86_64