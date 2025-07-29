FROM ruby:3.1-slim

# Install dependencies
RUN apt update && apt install -y \
  python3 \
  python3-pip \
  python3-venv \
  git \
  build-essential \
  libcurl4-openssl-dev \
  libssl-dev \
  libxml2 \
  libxml2-dev \
  libxslt1-dev \
  zlib1g-dev \
  libsqlite3-dev \
  && rm -rf /var/lib/apt/lists/*

# Install WPScan
RUN gem install wpscan

# Create and activate a virtual environment
WORKDIR /app
COPY . .

# Create virtual environment and install Python packages inside it
RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Start app using gunicorn from the virtualenv
CMD ["venv/bin/gunicorn", "app:app", "--bind", "0.0.0.0:10000"]
