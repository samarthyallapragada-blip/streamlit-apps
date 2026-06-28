import streamlit as st
import google.generativeai as genai

st.title("🤖 Gemini Chatbot")
st.caption("Chat with Google's Gemini AI")

api_key = st.text_input("Enter your Gemini API key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    
    # List available models
    available_models = []
    for m in genai.list_models():
        if "generateContent" in m.supported_generation_methods:
            available_models.append(m.name)
    
    if available_models:
        model_name = st.selectbox("Choose a model:", available_models)
        model = genai.GenerativeModel(model_name)

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

            try:
                response = model.generate_content(prompt)
                reply = response.text
            except Exception as e:
                reply = f"Error: {e}"

            st.session_state.messages.append({"role": "assistant", "content": reply})
            with st.chat_message("assistant"):
                st.write(reply)
    else:
        st.error("No models found. Check your API key.")
else:
    st.info("Please enter your Gemini API key to start chatting.")
