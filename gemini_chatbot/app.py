import streamlit as st
import google.generativeai as genai

st.title("🤖 Gemini Chatbot")
st.caption("Chat with Google's Gemini AI")

api_key = st.text_input("Enter your Gemini API key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    prompt = st.chat_input("Ask Gemini...")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        response = model.generate_content(prompt)
        reply = response.text

        st.session_state.messages.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant"):
            st.write(reply)
else:
    st.info("Please enter your Gemini API key to start chatting.")
