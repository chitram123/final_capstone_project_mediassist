import streamlit as st
import requests
import time
import os


# Page Config
st.set_page_config(
    page_title="MediAssist AI",
    layout="wide"
)

#chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

#fetching files from
RAW_DATA_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../data/raw_data"
    )
)
#title 
st.markdown("""
<style>
.block-container {
                padding-top: 1.2rem;
            color:#0F4C81;

}
</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <h1 style='text-align: center;'>
        MediAssist AI
    </h1>
    """,
    unsafe_allow_html=True
)

st.divider()

# 30% / 70% Layout
left_col, right_col = st.columns([3, 7])

# ==================================================
# LEFT PANEL
# ==================================================
with left_col:
    with st.container(border=True):

        st.markdown(
        """
        <h4 style='text-align: left;'>
        Upload Documents
        </h4>
        """,
        unsafe_allow_html=True
        )

        uploaded_file = st.file_uploader(
        "Choose File",
        type=["pdf", "docx", "txt"]
        )

        if uploaded_file is not None:

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
                success_message = st.empty()
                success_message.success("Document uploaded successfully")
                time.sleep(3)
                success_message.empty()
                #st.rerun()

        st.divider()

        st.markdown(
         """
        <h4 style='text-align: left;'>
        Uploaded Documents
        </h4>
        """,
        unsafe_allow_html=True
        )

        uploaded_files = []

        if os.path.exists(RAW_DATA_DIR):

            uploaded_files = sorted(
            os.listdir(RAW_DATA_DIR)
            )

        if uploaded_files:

            for index, file_name in enumerate(
            uploaded_files,
            start=1
            ):

                st.write(
                f"{index}. {file_name}"
                )

        else:

            st.write(
            "No documents uploaded"
            )

        st.divider()

        st.markdown(
        """
        <h6 style='text-align: left;'>
        Sources
        </h6>
        """,
        unsafe_allow_html=True
        )

        st.markdown("""
        <small>
        1. RAG on External Data<br>
        2. Multimodal Image<br>
        3. Database
        </small>
        """, unsafe_allow_html=True)

# ==================================================
# RIGHT PANEL
# ==================================================
with right_col:
    with st.container(border=True):
        st.write(
        "Ask questions about uploaded documents"
        )

        question = st.text_input(
        "Enter your question"
        )

        if st.button("Ask"):

            if question.strip() == "":

                st.warning(
                "Please enter a question"
                )

            else:

                response = requests.post(
                "http://127.0.0.1:8000/chat",
                json={
                    "question": question
                }
                )

                if response.status_code == 200:

                    answer = response.json()[
                    "answer"
                    ]

                    st.session_state.chat_history.append(
                    {
                    "question": question,
                    "answer": answer
                    }
                    )
                    st.rerun()
                else:

                    st.error(
                    "Failed to get response from chatbot"
                    )
    ###
        st.divider()

        st.markdown(
        """
        <h4>
        Conversation History
        </h4>
        """,
        unsafe_allow_html=True
        )

        for chat in st.session_state.chat_history:
        
            st.markdown(
            f"**You:** {chat['question']}"
            )

            st.markdown(
            f"**MediAssist:** {chat['answer']}"
            )

            st.divider()


    ###