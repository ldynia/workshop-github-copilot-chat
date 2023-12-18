# Flask Init

Boilerplate for a Flask application.

## Local Installation

```shell
pip install -r app/requirements.txt

export FLASK_APP=$PWD/app/run.py

flask run --host 0.0.0.0 --port 8080 --reload
```

## Docker Installation

```shell
# Building and running docker container
docker build -t flask-init --build-arg FLASK_DEBUG=True .
docker run -d --name flask-app -p 80:8080 --rm flask-init
docker ps
```

## API

```shell
curl "http://localhost"; echo
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
docker stop flask-app
```
