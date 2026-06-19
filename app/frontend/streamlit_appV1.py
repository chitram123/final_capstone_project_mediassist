import streamlit as st
import requests

st.title("MediAssist AI")

# Upload Section
uploaded_file = st.file_uploader(
    "Upload Document",
    type=["pdf","txt","docx"]
)

if uploaded_file:

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file,
            uploaded_file.type
        )
    }

    response = requests.post(
        "http://127.0.0.1:8000/upload",
        files=files
    )

    if response.status_code == 200:
        st.success(
            "Document uploaded successfully"
        )

# Question Section
question = st.text_input(
    "Ask a Question"
)

if st.button("Ask"):

    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json={
            "question": question
        }
    )

    if response.status_code == 200:

        answer = response.json()["answer"]

        st.write("### Answer")
        st.write(answer)