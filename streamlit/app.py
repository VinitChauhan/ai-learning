import streamlit as st

def main():
    st.title("AI Learning Application")
    st.write("Welcome to the AI Learning Application!")
    
    # User input for learning topics
    topic = st.selectbox("Select a topic to learn about:", ["Machine Learning", "Deep Learning", "Natural Language Processing"])
    
    if st.button("Learn"):
        st.write(f"You selected: {topic}")
        # Here you can add more interactive elements or content based on the selected topic

if __name__ == "__main__":
    main()