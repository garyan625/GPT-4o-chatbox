import streamlit as st
from google import genai

# 1. Page Configuration
st.set_page_config(page_title="Gemini-Chat", page_icon="🤖", layout="centered")

# 2. Persistence: Initialize Client
@st.cache_resource
def get_client():
    return genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

client = get_client()

# 3. Sidebar: Settings & Controls
st.sidebar.title("Settings")

# USE CURRENT STABLE MODEL NAMES
model_options = ["gemini-2.5-flash", "gemini-3.5-flash", "gemini-2.5-pro"]
model_choice = st.sidebar.selectbox("Choose Model", model_options)

# Reset chat session if model selection changes
if "current_model" not in st.session_state or st.session_state.current_model != model_choice:
    st.session_state.current_model = model_choice
    st.session_state.chat = client.chats.create(model=model_choice)
    st.session_state.chat_history = []

# Clear Chat Button
if st.sidebar.button("Clear Chat History"):
    st.session_state.chat_history = []
    st.session_state.chat = client.chats.create(model=model_choice)
    st.rerun()

# 4. Multimodal: Image Upload
uploaded_file = st.sidebar.file_uploader("Upload Image (Optional)", type=["jpg", "png", "jpeg"])

st.title("Gemini-Chat")

# Display Chat History
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Interaction: User Input & Streaming Response
if user_prompt := st.chat_input("Ask Gemini..."):
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    with st.spinner("Thinking..."):
        try:
            contents = [user_prompt]
            if uploaded_file:
                image_bytes = uploaded_file.getvalue()
                contents.append({"mime_type": "image/jpeg", "data": image_bytes})

            # Streamed Response
            with st.chat_message("assistant"):
                response_stream = st.session_state.chat.send_message_stream(contents)
                
                # Create a helper generator to extract ONLY the text content
                def stream_text():
                    for chunk in response_stream:
                        if chunk.text:
                            yield chunk.text
                
                # Write the text chunks
                assistant_response = st.write_stream(stream_text())
            
            st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
        except Exception as e:
            st.error(f"An error occurred: {e}")

# 6. Export History
if st.session_state.chat_history:
    chat_text = "\n".join([f"{msg['role'].upper()}: {msg['content']}" for msg in st.session_state.chat_history])
    st.sidebar.download_button(
        label="Download Chat History",
        data=chat_text,
        file_name="chat_history.txt",
        mime="text/plain"
    )
