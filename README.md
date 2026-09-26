# Student Management System

A full-stack application for managing student records, built with Python, Flask, Streamlit, and MySQL.

## Architecture

The application consists of four main components:
- **Backend**: Flask service handling database operations
- **Flask**: Middleware service that proxies requests to the backend
- **Streamlit**: Frontend UI for user interaction
- **MySQL**: Database for storing student records

## Project Structure

```
ai-learning/
├── backend/
│   ├── app.py              # Flask backend application
│   ├── Dockerfile          # Backend container configuration
│   └── requirements.txt    # Python dependencies
│
├── flask-app/
│   ├── app.py              # Flask middleware application
│   ├── Dockerfile          # Flask container configuration
│   └── requirements.txt    # Python dependencies
│
├── streamlit/
│   ├── app.py              # Streamlit frontend application
│   ├── Dockerfile          # Streamlit container configuration
│   └── requirements.txt    # Python dependencies
│
├── mysql/
│    └── init/                # Database initialization scripts
│        └── docker-entrypoint-initdb.sql
│
├── k8s/                    # Kubernetes deployment files
│   ├── mysql-deployment.yaml
│   ├── backend-deployment.yaml
│   ├── flask-deployment.yaml
│   ├── streamlit-deployment.yaml
│   ├── mysql-init-configmap.yaml
│   └── dashboard-admin.yaml
│
├── docker-compose.yml      # Docker Compose configuration
├── push-images.sh         # Script for pushing Docker images
└── README.md              # Project documentation
```

### Key Components

1. **Backend Service** (`backend/`)
   - Flask application handling database operations
   - RESTful API endpoints for CRUD operations
   - MySQL database connection and queries

2. **Flask Middleware** (`flask-app/`)
   - Proxies requests between the frontend and the backend
   - Adds CORS and an HTML landing page
   - Forwards CRUD calls to the backend's REST API

3. **Streamlit Frontend** (`streamlit/`)
   - User interface for student management
   - Real-time data updates
   - Interactive forms and tables

4. **Database** (`mysql/`)
   - MySQL database configuration
   - Initialization scripts for table creation
   - Sample data insertion

5. **Kubernetes Configurations** (`k8s/`)
   - Deployment configurations for all services
   - Service definitions
   - ConfigMaps for initialization
   - Dashboard access configuration

6. **Docker Configuration**
   - Individual Dockerfiles for each service
   - Docker Compose for local development
   - Image push script for container registry

## Prerequisites

- Docker Desktop
- Kubernetes (Kind) for local cluster
- kubectl
- GitHub Personal Access Token (for Docker image management)

## Setup Instructions

### 1. Docker Compose Setup (Development)

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ai-learning
   ```

2. Create a GitHub Personal Access Token:
   - Go to GitHub Settings > Developer Settings > Personal Access Tokens
   - Create a new token with `read:packages` scope
   - Login to GitHub Container Registry:
     ```bash
     echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin
     ```

3. Start the application:
   ```bash
   docker-compose up -d
   ```

4. Access the application:
   - Streamlit UI: http://localhost:8501
   - Flask API: http://localhost:5002
   - Backend API: http://localhost:5001

### 2. Kubernetes Setup (Production-like)

1. Install Kind:
   ```bash
   brew install kind
   ```

2. Create a local Kubernetes cluster:
   ```bash
   kind create cluster --name ai-learning-cluster
   ```

3. Load Docker images into Kind:
   ```bash
   kind load docker-image ghcr.io/vinitchauhan/ai-learning:backend ghcr.io/vinitchauhan/ai-learning:flask ghcr.io/vinitchauhan/ai-learning:streamlit --name ai-learning-cluster
   ```

4. Deploy the application:
   ```bash
   kubectl apply -f k8s/mysql-init-configmap.yaml
   kubectl apply -f k8s/mysql-deployment.yaml
   kubectl apply -f k8s/backend-deployment.yaml
   kubectl apply -f k8s/flask-deployment.yaml
   kubectl apply -f k8s/streamlit-deployment.yaml
   ```

5. Access the application:
   - Streamlit UI:
     ```bash
     kubectl port-forward service/streamlit 8501:8501
     ```
     Then visit: http://localhost:8501

   - Flask API:
     ```bash
     kubectl port-forward service/flask 5002:5002
     ```
     Then visit: http://localhost:5002

   - Backend API:
     ```bash
     kubectl port-forward service/backend 5001:5001
     ```
     Then visit: http://localhost:5001

### 3. Kubernetes Dashboard Access

1. Install the Kubernetes Dashboard:
   ```bash
   kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml
   ```

2. Create admin user:
   ```bash
   kubectl apply -f k8s/dashboard-admin.yaml
   ```

3. Start the dashboard proxy:
   ```bash
   kubectl proxy
   ```

4. Access the dashboard:
   - Open: http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/
   - Get the token:
     ```bash
     kubectl -n kubernetes-dashboard create token admin-user
     ```
   - Use the token to log in

## Application Features

- Add new students with name, email, and age
- View list of all students
- Edit student information
- Delete student records
- Real-time updates
- Responsive UI

## API Endpoints

### Backend API (Port 5001)
- `GET /api/students`: Get all students
- `GET /api/students/<id>`: Get a single student by id
- `POST /api/students`: Add new student
- `PUT /api/students/<id>`: Update student
- `DELETE /api/students/<id>`: Delete student
- `GET /test-db`: Health check / verify DB connection

### Flask API (Port 5002)
- `GET /students`: Get all students
- `POST /students/new`: Add new student
- `POST /students/{id}/edit`: Update student
- `POST /students/{id}/delete`: Delete student

## Database Schema

```sql
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    age INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

## Troubleshooting

1. If MySQL pod is stuck in Pending state:
   ```bash
   kubectl describe pod -l app=mysql
   ```

2. To check pod logs:
   ```bash
   kubectl logs -l app=<service-name>
   ```

3. To restart a deployment:
   ```bash
   kubectl rollout restart deployment/<deployment-name>
   ```

## Cleanup

### Docker Compose
```bash
docker-compose down
```

### Kubernetes
```bash
kind delete cluster --name ai-learning-cluster
```