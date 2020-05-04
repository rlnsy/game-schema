# Using django Dockerfile structure per this post:
# https://medium.com/backticks-tildes/how-to-dockerize-a-django-application-a42df0cb0a99

FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /game_schema_poc
ADD . /game_schema_poc/
WORKDIR /game_schema_poc
RUN pip install -r requirements.txt
ENTRYPOINT ["/game_schema_poc/docker_entry.sh"]
