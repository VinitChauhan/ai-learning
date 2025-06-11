import streamlit as st
import requests
import json

# Flask API endpoints
FLASK_API_URL = "http://flask:5002"  # Updated to use correct service name and port from docker-compose.yml

def fetch_students():
    try:
        response = requests.get(f"{FLASK_API_URL}/students")
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error fetching students: {response.text}")
            return []
    except Exception as e:
        st.error(f"Error connecting to Flask backend: {str(e)}")
        return []

def add_student(name, email, age):
    try:
        data = {"name": name, "email": email, "age": age}
        response = requests.post(f"{FLASK_API_URL}/students/new", json=data)
        if response.status_code == 200:
            st.success("Student added successfully!")
            return True
        else:
            st.error(f"Error adding student: {response.text}")
            return False
    except Exception as e:
        st.error(f"Error connecting to Flask backend: {str(e)}")
        return False

def update_student(student_id, name, email, age):
    try:
        data = {"name": name, "email": email, "age": age}
        response = requests.post(f"{FLASK_API_URL}/students/{student_id}/edit", json=data)
        if response.status_code == 200:
            st.success("Student updated successfully!")
            return True
        else:
            st.error(f"Error updating student: {response.text}")
            return False
    except Exception as e:
        st.error(f"Error connecting to Flask backend: {str(e)}")
        return False

def delete_student(student_id):
    try:
        response = requests.post(f"{FLASK_API_URL}/students/{student_id}/delete")
        if response.status_code == 200:
            st.success("Student deleted successfully!")
            return True
        else:
            st.error(f"Error deleting student: {response.text}")
            return False
    except Exception as e:
        st.error(f"Error connecting to Flask backend: {str(e)}")
        return False

def main():
    st.title("Student Management System")
    
    # Sidebar for adding new students
    with st.sidebar:
        st.header("Add New Student")
        with st.form("add_student_form"):
            new_name = st.text_input("Name")
            new_email = st.text_input("Email")
            new_age = st.number_input("Age", min_value=1, max_value=120, value=18)
            submit_button = st.form_submit_button("Add Student")
            
            if submit_button:
                if add_student(new_name, new_email, new_age):
                    st.rerun()

    # Main content area
    st.header("Student List")
    
    # Fetch and display students
    students = fetch_students()
    
    if students:
        # Create a table with student data
        for student in students:
            with st.expander(f"{student['name']} - {student['email']}"):
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    # Edit form
                    with st.form(f"edit_form_{student['id']}"):
                        st.subheader("Edit Student")
                        edit_name = st.text_input("Name", value=student['name'], key=f"name_{student['id']}")
                        edit_email = st.text_input("Email", value=student['email'], key=f"email_{student['id']}")
                        edit_age = st.number_input("Age", value=student['age'], min_value=1, max_value=120, key=f"age_{student['id']}")
                        update_button = st.form_submit_button("Update")
                        
                        if update_button:
                            if update_student(student['id'], edit_name, edit_email, edit_age):
                                st.rerun()
                
                with col2:
                    # Delete button
                    if st.button("Delete", key=f"delete_{student['id']}"):
                        if delete_student(student['id']):
                            st.rerun()
    else:
        st.info("No students found. Add some students using the sidebar form.")

if __name__ == "__main__":
    main()
