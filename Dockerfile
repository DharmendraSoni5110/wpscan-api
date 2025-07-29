FROM debian:bookworm

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-dev python3-pip python3-venv python3-setuptools \
    ruby-full build-essential libcurl4-openssl-dev \
    libssl-dev zlib1g-dev liblzma-dev git curl && \
    gem install wpscan && \
    pip3 install --upgrade pip

# Run WPScan update to cache the vulnerability DB in image
RUN wpscan --update || true

# Set working directory
WORKDIR /app

# Copy application code
COPY . .

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Expose the correct port (Render detects this)
EXPOSE 10000

# Start the app with increased timeout (for large scans)
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000", "--timeout", "600"]
