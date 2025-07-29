
FROM ruby:3.2

RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    libcurl4-openssl-dev libpq-dev \
    git build-essential

RUN gem install wpscan

WORKDIR /app
COPY . .

RUN pip3 install -r requirements.txt

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]
