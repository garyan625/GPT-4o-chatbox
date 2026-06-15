import os
import json
import streamlit as st
from google import genai

# Load configuration
working_dir = os.path.dirname(os.path.realpath(__file__))
config_path = f"{working_dir}/config.json"
with open(config_path) as f:
    config_data = json.load(f)

# Initialize the new Gemini Client
client = genai.Client(api_key=config_data["GEMINI_API_KEY"].strip())

# Page configuration
st.set_page_config(
    page_title="Gemini-Chat",
    page_icon="🤖",
    layout="centered"
)

st.title("Gemini-Chat")

# Initialize chat session in session_state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_prompt = st.chat_input("Ask Gemini...")

if user_prompt:
    # 1. Add user prompt to display
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # 2. Get response from Gemini using the new SDK
    with st.spinner("Thinking..."):
        try:
            # Create a persistent chat session
            chat = client.chats.create(model="gemini-3.5-flash")

            # Replay history into the chat object so it remembers context
            for msg in st.session_state.chat_history[:-1]:
                role = "user" if msg["role"] == "user" else "model"
                chat.send_message(msg["content"])

            # Send current message
            response = chat.send_message(user_prompt)
            assistant_response = response.text

            # 3. Store and display response
            st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
            with st.chat_message('assistant'):
                st.markdown(assistant_response)

        except Exception as e:
            st.error(f"An error occurred: {e}")