FROM python:3.10-bullseye
LABEL maintainer="Jabba"

ENV PYTHONUNBUFFERED 1

COPY ./celery-build/requirements.txt /requirements.txt
COPY ./app /app
COPY ./celery-build/scripts /scripts

WORKDIR /app

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt && \
    adduser celery && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER celery

CMD [ "run.sh" ]
