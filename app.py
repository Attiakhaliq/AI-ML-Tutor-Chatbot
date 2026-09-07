import streamlit as st

import requests


st.title ("👩‍💻AI & MAchine Learning Tutor")


# Chat History

if "messages" not in st.session_state:
    st.session_state.messages = []


if st.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.rerun()






for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])



user_message = st.chat_input(" Ask me anything about AI & Machine Learning...")


if user_message:

    with st.chat_message("user"):
        st.write(user_message)

    st.session_state.messages.append ({
        "role": "user",
        "content": user_message
    })

   
try:
    response = requests.post("http://127.0.0.1:8000/chat", json={"message": user_message},
                             timeout=60)

    response.raise_for_status()


    data = response.json()

    st.write(data["response"])

    with st.chat_message("assistant"):
        st.write("answer: ", data["response"])

    st.session_state.messages.append({ "role": "assistant", 
                                        "content": data["response"]})

except requests.exceptions.RequestException:
    answer = "Sorry, I am unable to process your request at the moment. Please try again later."

except Exception:
    answer = "Sorry, Something went wrong."