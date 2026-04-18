import streamlit as st
import os
from google import genai
from google.genai import types
from prompts import SYSTEM_INSTRUCTION
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

st.set_page_config(page_title="StadiumAI Assistant", page_icon="🏟️", layout="centered")

st.title("🏟️ StadiumAI")
st.markdown("Welcome! I'm your smart guide for food, navigation, schedules, and more at the stadium.")

# Ensure API key is available
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    st.error("Missing GEMINI_API_KEY environment variable. Please check your .env file.")
    st.stop()

# Initialize Gemini Client
@st.cache_resource
def get_client():
    return genai.Client(api_key=api_key)

client = get_client()

# Initialize chat session
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat messages
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("How can I help you at the stadium today?"):
    # Store user message
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # Build contents array for Gemini
        contents = []
        for msg in st.session_state.chat_history:
            role = "user" if msg["role"] == "user" else "model"
            contents.append(
                types.Content(
                    role=role,
                    parts=[types.Part.from_text(text=msg["content"])]
                )
            )
        
        with st.spinner("StadiumAI is thinking..."):
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=contents,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_INSTRUCTION,
                    temperature=0.7,
                )
            )
        
        assistant_reply = response.text
        
        # Store and display assistant response
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_reply})
        with st.chat_message("assistant"):
            st.markdown(assistant_reply)

    except Exception as e:
        st.error(f"An error occurred: {e}")