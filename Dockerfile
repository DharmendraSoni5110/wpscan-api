FROM python:3.10-slim

RUN apt update && apt install -y \
    ruby-full \
    git \
    curl \
    build-essential \
    libcurl4-openssl-dev \
    libssl-dev \
    zlib1g-dev \
    libxml2-dev \
    libxslt1-dev \
    libyaml-dev \
    libgmp-dev \
    libreadline-dev \
    libncurses5-dev \
    libffi-dev \
    libsqlite3-dev \
    wget \
    && gem install wpscan \
    && pip install flask gunicorn

COPY . /app
WORKDIR /app

CMD ["gunicorn", "-b", "0.0.0.0:10000", "app:app"]
