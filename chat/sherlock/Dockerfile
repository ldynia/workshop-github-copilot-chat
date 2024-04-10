FROM python:3.9.5-alpine

ARG FLASK_DEBUG=False \
    WORKDIR=/usr/src/app

ENV FLASK_APP=$WORKDIR/run.py \
    FLASK_DEBUG=$FLASK_DEBUG \
    HOST=0.0.0.0 \
    PORT=8080 \
    PYTHONUNBUFFERED=True

WORKDIR $WORKDIR
COPY app/ $WORKDIR

RUN apk add curl

RUN python -m pip install --upgrade pip --requirement requirements.txt

CMD flask run --host=$HOST --port=$PORT
