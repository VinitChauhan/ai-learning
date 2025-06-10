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

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd ai-learning
   ```

2. **Build and run the application**:
   Use Docker Compose to build and run the services:
   ```
   docker-compose up --build
   ```

3. **Access the applications**:
   - Streamlit app: Open your browser and go to `http://localhost:8501`
   - Flask app: Access the API at `http://localhost:5000`

## Usage

- Interact with the Streamlit application to visualize and manipulate data.
- Use the Flask API to send requests and receive responses from the backend.
- The backend connects to a MySQL database to store and retrieve data.

## Additional Information

- Ensure that Docker and Docker Compose are installed on your machine.
- Modify the `requirements.txt` files in the `flask-app` and `backend` directories to add any additional dependencies as needed.
- Customize the application logic in the respective `app.py` files for each component.
