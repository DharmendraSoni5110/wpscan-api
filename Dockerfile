FROM ruby:3.1

RUN apt-get update && apt-get install -y \
  curl git python3 python3-pip build-essential libcurl4-openssl-dev \
  libssl-dev zlib1g-dev libsqlite3-dev libxml2 libxml2-dev \
  libxslt-dev libyaml-dev libgmp-dev libreadline-dev

RUN gem install wpscan

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 10000

CMD ["gunicorn", "-b", "0.0.0.0:10000", "app:app"]
