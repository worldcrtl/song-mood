import streamlit as st



name = st.text_input("What's your name?")
age = int(st.number_input("How old are you?"))

if name:
    st.write(f"Hello, {name}! 👋")
if age < 40:
    st.write(f"You are {age} years old.")
else:
    st.write(f"You are {age} years old. That's great!")

file = st.file_uploader("Upload a file")
if file is not None:
    st.write("File uploaded successfully!")
    st.write(f"**Filename:** {file.name}")
    st.write(f"**File type:** {file.type}")
    st.write(f"**File size:** {file.size} bytes")
    
    # Display file content based on type
    if file.type.startswith("image/"):
        st.image(file, caption=file.name)
    elif file.type == "text/plain" or file.type == "text/csv":
        st.text(file.read().decode("utf-8"))
    elif "pdf" in file.type:
        st.pdf(data=file, filename=file.name)
    else:
        st.download_button(
            label="Download file",
            data=file,
            file_name=file.name,
            mime=file.type
        )
else:
    st.write("No file uploaded yet.")

