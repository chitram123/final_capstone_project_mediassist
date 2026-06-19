from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader
)
import os
def load_doc(file_path):
    if file_path.endswith(".pdf"):
    # Load PDF
        loader = PyPDFLoader(file_path)

    elif file_path.endswith(".docx"):
    #load docx
        loader = Docx2txtLoader(file_path)

    elif file_path.endswith(".txt"):
    #load txt
        loader = TextLoader(file_path)

    else:
        print(f"Unsupported file format: {file_path}")
        return []

    return loader.load()

