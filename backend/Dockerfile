FROM python:3.10-slim-bullseye

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    default-mysql-client \
    gcc \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip setuptools

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
