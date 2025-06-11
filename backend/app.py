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

@app.route('/api/data', methods=['GET'])
def get_data():
    connection = get_mysql_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM my_table')
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(results)

@app.route('/api/data', methods=['POST'])
def create_data():
    new_data = request.json
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO my_table (column1, column2) VALUES (%s, %s)', 
                   (new_data['column1'], new_data['column2']))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify(new_data), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)