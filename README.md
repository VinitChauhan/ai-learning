# AI Learning Project

This project is designed to demonstrate a simple application architecture using Streamlit, Flask, and a backend service with MySQL. The application consists of three main components:

1. **Streamlit**: A web application framework for creating interactive data applications. The Streamlit app serves as the frontend interface for users to interact with the data.

2. **Flask**: A lightweight WSGI web application framework in Python. The Flask app acts as a RESTful API that handles requests from the Streamlit frontend and communicates with the backend.

3. **Backend**: This component contains the business logic and interacts with a MySQL database. It processes data and serves it to the Flask API.

## Project Structure

```
ai-learning
├── streamlit
│   └── app.py          # Streamlit application code
├── flask-app
│   ├── app.py          # Flask application entry point
│   └── requirements.txt # Dependencies for Flask app
├── backend
│   ├── app.py          # Backend application code
│   └── requirements.txt # Dependencies for backend app
├── docker-compose.yml   # Docker Compose configuration
└── README.md            # Project documentation
```
## Services
- **Streamlit**: Frontend UI (Port 8501)
- **Flask**: API Service (Port 5000)
- **Backend**: Database Service (Port 5001)
- **MySQL**: Database (Port 3306) 


## Prerequisites
- Docker
- Docker Compose
- Git

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/VinitChauhan/ai-learning.git
cd ai-learning
```

2. Start the services:
```bash
docker compose up -d
```

3. Access the applications:
- Streamlit UI: http://localhost:8501
- Flask API: http://localhost:5000
- Backend API: http://localhost:5001

## Environment Variables
### Flask Service
- FLASK_ENV=development
- PYTHONHTTPSVERIFY=0
- REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
- SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

### Backend Service
- MYSQL_HOST=mysql
- MYSQL_USER=root
- MYSQL_PASSWORD=root
- MYSQL_DATABASE=mydatabase

### MySQL Service
- MYSQL_ROOT_PASSWORD=root
- MYSQL_DATABASE=mydatabase

## Docker Images
All images are available on Docker Hub under the repository:
- vinitjava/my-ai-learning:streamlit
- vinitjava/my-ai-learning:flask
- vinitjava/my-ai-learning:backend

## Development

To rebuild services:
```bash
docker compose build
```

To view logs:
```bash
docker compose logs -f
```

## Database
MySQL data is persisted using Docker volumes:
- mysql_data: Database files
- ./mysql/init: Initialization scripts

## Networking
Services communicate through the 'app-network' bridge network.


## Usage

- Interact with the Streamlit application to visualize and manipulate data.
- Use the Flask API to send requests and receive responses from the backend.
- The backend connects to a MySQL database to store and retrieve data.

## Additional Information

- Ensure that Docker and Docker Compose are installed on your machine.
- Modify the `requirements.txt` files in the `flask-app` and `backend` directories to add any additional dependencies as needed.
- Customize the application logic in the respective `app.py` files for each component.

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
