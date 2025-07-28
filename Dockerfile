# Use base Ubuntu image
FROM ubuntu:22.04

# Install system packages
RUN apt update && apt install -y \
    ruby-full \
    build-essential \
    git \
    curl \
    python3 \
    python3-pip \
    python3-venv \
    libcurl4-openssl-dev \
    libssl-dev \
    zlib1g-dev \
    libxml2-dev \
    libxslt1-dev \
    libreadline-dev \
    libyaml-dev \
    libsqlite3-dev \
    sqlite3 \
    gnupg \
    lsb-release \
    unzip

# Install WPScan via gem
RUN gem install wpscan

# Set up Python environment
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy the app code
COPY wpscan_api.py .

# Expose port
EXPOSE 10000

# Start with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "wpscan_api:app"]
