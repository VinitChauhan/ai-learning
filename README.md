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
- **Flask**: API Service (Port 5002)
- **Backend**: Database Service (Port 5001)
- **MySQL**: Database (Port 3306) 

1. **Streamlit Frontend** (Port 8501)
   - Modern UI for student management
   - Real-time data updates
   - Interactive forms and tables
2. **Flask Middleware** (Port 5002)
   - Handles API requests from Streamlit
   - Communicates with the backend service
   - Provides CORS support

3. **Backend Service** (Port 5001)
   - Core business logic
   - Database operations
   - RESTful API endpoints

4. **MySQL Database** (Port 3306)
   - Persistent data storage
   - Student information management

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

2. Start and Stop services:
```bash
docker-compose down
docker-compose build
docker-compose up -d
```

3. Access the applications:
- Streamlit UI: http://localhost:8501
- Flask API: http://localhost:5002
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
- ai-learning:streamlit
- ai-learning:flask
- ai-learning:backend

## Features

### Student Management
- View all students in a responsive table
- Add new students with validation
- Edit existing student information
- Delete students with confirmation
- Real-time updates after operations

### API Endpoints

#### Flask API (http://localhost:5002)
- `GET /students` - Get all students
- `POST /students/new` - Create a new student
- `POST /students/{id}/edit` - Update a student
- `POST /students/{id}/delete` - Delete a student

#### Backend API (http://localhost:5001)
- `GET /api/students` - Get all students
- `POST /api/students` - Create a new student
- `PUT /api/students/{id}` - Update a student
- `DELETE /api/students/{id}` - Delete a student

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


### Adding New Features

1. **Frontend (Streamlit)**
   - Add new UI components in `streamlit/app.py`
   - Use Streamlit's built-in components for forms and tables

2. **Middleware (Flask)**
   - Add new routes in `flask-app/app.py`
   - Update CORS settings if needed
   - Add new API endpoints

3. **Backend**
   - Add new business logic in `backend/app.py`
   - Create new database tables if needed

## Troubleshooting

### Common Issues

1. **Connection Issues**
   - Ensure all services are running: `docker-compose ps`
   - Check service logs: `docker-compose logs <service-name>`
   - Verify network connectivity between services

2. **Database Issues**
   - Check MySQL connection: `docker-compose logs mysql`
   - Verify database initialization scripts
   - Check database credentials in environment variables

3. **API Issues**
   - Verify API endpoints are accessible
   - Check CORS configuration
   - Review API response formats

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
