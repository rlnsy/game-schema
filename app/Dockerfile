# Using django Dockerfile structure per this post:
# https://medium.com/backticks-tildes/how-to-dockerize-a-django-application-a42df0cb0a99

FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
ADD . /app/
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["/app/docker_entry.sh"]
