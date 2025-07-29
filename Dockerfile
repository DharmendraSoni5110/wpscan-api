FROM debian:bookworm

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-venv python3-pip \
    ruby-full build-essential libcurl4-openssl-dev \
    libssl-dev zlib1g-dev liblzma-dev git curl && \
    gem install wpscan

# Set workdir
WORKDIR /app

# Create Python virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip (now safe inside venv)
RUN pip install --upgrade pip

# Copy code and install dependencies
COPY . /app
RUN pip install -r requirements.txt

# Preload WPScan database to avoid scan_aborted errors
RUN wpscan --update || true

# Expose the port (Render will detect this)
EXPOSE 10000

# Start the Flask app with gunicorn, long timeout for big scans
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000", "--timeout", "600"]
