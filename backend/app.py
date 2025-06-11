from flask import Flask, jsonify, request
import mysql.connector
import os

app = Flask(__name__)

# Database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', ''),
        database=os.getenv('DB_NAME', 'mydatabase')
    )
    return connection

def get_mysql_connection():
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host="mysql",  # container name from docker-compose
        user="root",
        password="root",
        database="mydatabase"
    )
    return connection

# Student CRUD Operations
@app.route('/api/students', methods=['GET'])
def get_students():
    try:
        connection = get_mysql_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM students')
        students = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(students)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    try:
        connection = get_mysql_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM students WHERE id = %s', (student_id,))
        student = cursor.fetchone()
        cursor.close()
        connection.close()
        if student:
            return jsonify(student)
        return jsonify({"error": "Student not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/students', methods=['POST'])
def create_student():
    try:
        data = request.json
        required_fields = ['name', 'email', 'age']
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400

        connection = get_mysql_connection()
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO students (name, email, age) VALUES (%s, %s, %s)',
            (data['name'], data['email'], data['age'])
        )
        connection.commit()
        student_id = cursor.lastrowid
        cursor.close()
        connection.close()
        
        return jsonify({
            "message": "Student created successfully",
            "student_id": student_id
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    try:
        data = request.json
        connection = get_mysql_connection()
        cursor = connection.cursor()
        
        # Check if student exists
        cursor.execute('SELECT id FROM students WHERE id = %s', (student_id,))
        if not cursor.fetchone():
            cursor.close()
            connection.close()
            return jsonify({"error": "Student not found"}), 404

        # Update student
        update_fields = []
        values = []
        for key, value in data.items():
            if key in ['name', 'email', 'age']:
                update_fields.append(f"{key} = %s")
                values.append(value)
        
        if not update_fields:
            return jsonify({"error": "No valid fields to update"}), 400

        values.append(student_id)
        query = f"UPDATE students SET {', '.join(update_fields)} WHERE id = %s"
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        
        return jsonify({"message": "Student updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    try:
        connection = get_mysql_connection()
        cursor = connection.cursor()
        
        # Check if student exists
        cursor.execute('SELECT id FROM students WHERE id = %s', (student_id,))
        if not cursor.fetchone():
            cursor.close()
            connection.close()
            return jsonify({"error": "Student not found"}), 404

        # Delete student
        cursor.execute('DELETE FROM students WHERE id = %s', (student_id,))
        connection.commit()
        cursor.close()
        connection.close()
        
        return jsonify({"message": "Student deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Existing endpoints
@app.route('/test-db', methods=['GET'])
def test_db_connection():
    try:
        connection = get_mysql_connection()
        if connection.is_connected():
            db_info = connection.get_server_info()
            cursor = connection.cursor()
            cursor.execute("select database();")
            db_name = cursor.fetchone()
            cursor.close()
            connection.close()
            return jsonify({
                "status": "success",
                "message": "Database connection successful",
                "server_info": db_info,
                "database": db_name[0]
            })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Database connection failed: {str(e)}"
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)