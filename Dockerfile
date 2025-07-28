FROM ubuntu:22.04

RUN apt update && apt install -y \
    ruby-full build-essential git curl \
    python3 python3-pip libcurl4-openssl-dev \
    libssl-dev zlib1g-dev libxml2-dev \
    libxslt1-dev libreadline-dev libyaml-dev \
    libsqlite3-dev sqlite3 gnupg lsb-release unzip

RUN gem install wpscan

WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY wpscan_api.py .

EXPOSE 10000

CMD ["gunicorn", "--bind", "0.0.0.0:10000", "wpscan_api:app"]
