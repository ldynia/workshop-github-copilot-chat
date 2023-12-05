# flask-init-mini

## Installation

```bash
# Building and running docker container
docker build --tag flask-mini --build-arg FLASK_DEBUG=True .
docker run --detach --name flask-app --publish 80:8080 --rm flask-mini
docker ps
```

## API

```bash
curl "http://localhost"; echo
```

## Testing

Unit test

```bash
docker exec flask-app pytest
```

Code coverage

```bash
docker exec flask-app coverage run -m pytest
docker exec flask-app coverage report
```

Stop container

```bash
docker stop flask-app
```