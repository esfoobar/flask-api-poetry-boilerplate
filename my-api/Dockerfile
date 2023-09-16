FROM ubuntu:20.04

ENV TZ=America//Los_Angeles
ENV DEBIAN_FRONTEND noninteractive

# Install packages
RUN apt-get update && apt-get install -y \
    build-essential \
    make \
    gcc \
    git \
    unzip \
    wget \
    openssl \
    libssl-dev \
    libffi-dev \
    postgresql-client \
    python3-dev \
    python3-pip

# Install Python 3.10
RUN wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz \
    && tar -xvf Python-3.10.0.tgz \
    && cd Python-3.10.0 \
    && ./configure --enable-optimizations \
    && make altinstall

# Set Python3 to be default
RUN apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update
RUN update-alternatives --install /usr/bin/python python /usr/local/bin/python3.10 1

ENV PIP_DISABLE_PIP_VERSION_CHECK=on

# Install poetry
RUN pip3 install poetry

# set "my_api" as the working directory from which CMD, RUN, ADD references
WORKDIR /my-api

# now copy all the files in this directory to /code
COPY . .

# setup poetry
COPY pyproject.toml /my-api/
RUN poetry env use 3.10 && poetry config virtualenvs.create true \
    && poetry config virtualenvs.in-project false \
    && poetry install --no-interaction

# Listen to port 5000 at runtime
EXPOSE 5000

# Define our command to be run when launching the container
CMD poetry run gunicorn my_api.wsgi:app -b 0.0.0.0:5000 --capture-output --enable-stdio-inheritance
