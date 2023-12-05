FROM python:3.9.5-alpine

# Build arguments
ARG FLASK_DEBUG=False \
    GROUP=nogroup \
    USER=nobody \
    WORKDIR=/usr/src

# Environment variables
ENV FLASK_APP=$WORKDIR/run.py \
    FLASK_DEBUG=$FLASK_DEBUG \
    HOST=0.0.0.0 \
    PORT=8080 \
    PYTHONUNBUFFERED=True

# App's file system
WORKDIR $WORKDIR
RUN chown $USER:$GROUP $WORKDIR
COPY --chown=$USER:$GROUP app/ $WORKDIR

# Install OS packages
RUN apk add vim

# Install python packages
RUN pip install --upgrade pip --requirement requirements.txt

# Expose app's port
EXPOSE $PORT

# Run rootless
USER $USER:$GROUP

# Start app
CMD flask run --host=$HOST --port=$PORT