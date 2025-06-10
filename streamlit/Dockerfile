FROM python:3.10

WORKDIR /app


# Install certificates and set SSL environment
ENV PYTHONHTTPSVERIFY=0
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
ENV SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

# Install dependencies with trusted hosts
COPY requirements.txt ./
RUN pip install --trusted-host pypi.org \
    --trusted-host files.pythonhosted.org \
    --no-cache-dir -r requirements.txt

COPY . .

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]