FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y default-mysql-client && \
    apt-get install -y gcc default-libmysqlclient-dev build-essential pkg-config && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip setuptools

COPY requirements.txt .
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

COPY . .

CMD ["python", "app.py"]