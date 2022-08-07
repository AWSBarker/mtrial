FROM python:3.9-alpine3.13
LABEL maintainer="awsb.ddns.net"

ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
COPY . mtrial

WORKDIR mtrial
EXPOSE 8000

RUN python -m venv /ve_django && \
    /ve_django/bin/pip install --upgrade pip && \
    /ve_django/bin/pip install -r requirements.txt && \
    adduser --disabled-password --no-create-home mtrial

ENV PATH="/ve_django/bin:$PATH"

USER mtrial

# runs the production server
#ENTRYPOINT ["python", "manage.py"]
#CMD ["runserver", "0.0.0.0:8001"]
