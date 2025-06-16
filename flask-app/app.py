from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import requests
import json
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.secret_key = 'your_secret_key'  # Required for flash messages

# Backend API URL - using environment variable with fallback
BACKEND_URL = os.getenv('BACKEND_URL', 'http://backend:5001')

@app.route('/')
def index():
    try:
        # Get all students
        response = requests.get(f"{BACKEND_URL}/api/students")
        students = response.json() if response.status_code == 200 else []
        return render_template('index.html', students=students)
    except Exception as e:
        flash(f"Error fetching students: {str(e)}", "error")
        return render_template('index.html', students=[])

@app.route('/students')
def get_students():
    try:
        response = requests.get(f"{BACKEND_URL}/api/students")
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": "Failed to fetch students"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/students/new', methods=['POST'])
def new_student():
    try:
        data = request.get_json()
        response = requests.post(f"{BACKEND_URL}/api/students", json=data)
        if response.status_code == 201:
            return jsonify({"message": "Student created successfully"})
        else:
            return jsonify({"error": response.json().get('error', 'Failed to create student')}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/students/<int:id>/edit', methods=['POST'])
def edit_student(id):
    try:
        data = request.get_json()
        response = requests.put(f"{BACKEND_URL}/api/students/{id}", json=data)
        if response.status_code == 200:
            return jsonify({"message": "Student updated successfully"})
        else:
            return jsonify({"error": response.json().get('error', 'Failed to update student')}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/students/<int:id>/delete', methods=['POST'])
def delete_student(id):
    try:
        response = requests.delete(f"{BACKEND_URL}/api/students/{id}")
        if response.status_code == 200:
            return jsonify({"message": "Student deleted successfully"})
        else:
            return jsonify({"error": response.json().get('error', 'Failed to delete student')}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)