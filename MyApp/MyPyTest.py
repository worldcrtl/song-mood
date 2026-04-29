import streamlit as st

st.title("Hello, World! 🌎")
st.write("Welcome to MyPyTest running in the browser!")

# Interactive elements
name = st.text_input("What's your name?")
age = st.number_input("What's your age?", min_value=0, max_value=150, value=0)

if input:
    st.success(f"Hello, {name}! 👋 You are {age} years old.")

# Current date/time
st.info(f"Today's date: {st.date_input('Select a date')}")
