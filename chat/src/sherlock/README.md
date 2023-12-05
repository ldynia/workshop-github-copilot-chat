# Flask Init

Boilerplate for a Flask application.

## Local Installation

```shell
pip install -r requirements.txt

export FLASK_APP=$PWD/run.py

flask run --host 0.0.0.0 --port 8080
```

## Docker Installation

```shell
# Building and running docker container
docker build --tag flask-sherlock --build-arg FLASK_DEBUG=True .
docker run --detach --name sherlock --publish 80:8080 --rm flask-sherlock
docker ps
```

## API

```shell
curl "http://localhost/livez"
curl "http://localhost/api/v1/movies/recommend?title=Kingpin"
curl "http://localhost/api/v1/movies/recommend?title=Lost%20in%20Translation"
```

## Testing

Unit test

```shell
docker exec flask-app pytest
docker exec flask-app coverage run -m pytest
docker exec flask-app coverage report
```

Stop container

```shell
docker stop flask-sherlock
```
