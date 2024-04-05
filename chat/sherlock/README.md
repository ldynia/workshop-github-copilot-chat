# Sherlock

A movie recommendation engine exposed via REST API written in Flask.

## Local Installation

**TIP:** Remember to fix PYTHONPATH first.

```shell
pip install -r app/requirements.txt
export FLASK_APP=$PWD/app/run.py
flask run --host 0.0.0.0 --port 8080 --reload
```

## Docker Installation

```shell
# Building and running docker container
docker build --tag flask-sherlock --build-arg FLASK_DEBUG=True .
docker run --detach --name sherlock --publish 8080:8080 --rm flask-sherlock
docker ps
```

## API

```shell
curl "http://localhost/"
curl "http://localhost/livez"
curl "http://localhost/api/v1/movies/recommend"
curl "http://localhost/api/v1/movies/recommend?title=Kingpin"
curl "http://localhost/api/v1/movies/recommend?title=Lost%20in%20Translation"
```

## Testing

Unit test

```shell
docker exec sherlock pytest
docker exec sherlock coverage run -m pytest
docker exec sherlock coverage report
```

Stop container

```shell
docker stop sherlock
```
