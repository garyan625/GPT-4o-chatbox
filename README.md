Gemini-Chat: Multimodal AI Assistant
Gemini-Chat is a responsive, web-based AI assistant built with Streamlit and the Google GenAI SDK. It provides a clean, user-friendly interface to interact with Google’s latest Gemini models, featuring support for text chat, image analysis, and session history management.

🚀 Features
Multimodal Interaction: Chat with Gemini using both text and image uploads.

Real-time Streaming: Experience fast, natural interactions with word-by-word streaming responses.

Persistent Context: The app remembers your conversation history throughout the session.

Model Selection: Switch between different Gemini models (e.g., gemini-2.5-flash, gemini-3.5-flash) directly from the sidebar.

History Management: Easily clear your chat session or download the full conversation history as a text file.

Secure Deployment: Built with industry-standard practices, including secure API key management via Streamlit Secrets.

🛠 Tech Stack
Frontend: Streamlit

AI Engine: Google GenAI SDK

Deployment: Streamlit Community Cloud

📦 Requirements
To run this project locally, ensure you have the following installed:

Python 3.10+

streamlit

google-genai

Install dependencies using:

Bash
pip install streamlit google-genai
⚙️ Setup and Configuration
Clone the repository:

git clone https://github.com/your-username/GPT-4o-chatbox.git
cd GPT-4o-chatbox


2.  **API Key:** 
    You need a Gemini API key from [Google AI Studio](https://aistudio.google.com/).

3.  **Secrets:**
    If running locally, create a `.streamlit/secrets.toml` file in your project root:
    ```toml
GEMINI_API_KEY = "your_actual_api_key_here"
Run the App:

streamlit run main.py


## 🌐 Deployment

This app is optimized for deployment on **Streamlit Community Cloud**:
1.  Connect your GitHub repository to [Streamlit Share](https://share.streamlit.io/).
2.  In your app **Settings > Secrets**, add:
    ```toml
GEMINI_API_KEY = "your_actual_api_key_here"
Deploy!

Built with ❤️ using Google Gemini.
