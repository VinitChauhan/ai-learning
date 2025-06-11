FROM python:3.10-slim-bullseye

WORKDIR /app

# Install certificates and set SSL environment
ENV PYTHONHTTPSVERIFY=1
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
ENV SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates && \
    update-ca-certificates && \
    apt-get install -y --no-install-recommends \
    default-mysql-client \
    gcc \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt /app/
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

# Copy the application files
COPY app.py /app/
COPY templates/ /app/templates/

CMD ["python", "app.py"]