import time

import streamlit as st
from dotenv import load_dotenv

from src.serving.utils import get_lmm

load_dotenv()


def stream_response(text: str):
    for word in text.split():
        yield word + " "
        time.sleep(0.05)


model = get_lmm()

st.header("AWS documentation assistant", divider="rainbow")
st.caption("Welcome to the AWS documentation assistant. Ask me anything about AWS and I will try to help you.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Your question here"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = model.invoke(prompt)
        st.write_stream(stream_response(response))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
