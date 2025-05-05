import streamlit as st

# Title and headers
st.title("My First Streamlit App")
st.header("Welcome to the Demo")
st.write("This app demonstrates basic Streamlit components.")

# Input fields
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, max_value=120, value=25)

# Display output
if name:
    st.write(f"Hello, {name}!")
st.write(f"Your age is {age}.")
