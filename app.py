# app.py (Streamlit version of TextLoom)
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="TextLoom", page_icon="✨", layout="centered")

st.title("✨ TextLoom")
st.subheader("Weaving AI text into natural human flow")

# Input
text_input = st.text_area("🤖 Enter AI-generated text", height=200)

# Tone selection
tone = st.selectbox(
    "🎨 Choose a tone",
    ["Conversational", "Professional", "Friendly", "Witty", "Casual", "Creative", "Academic"]
)

if st.button("✨ Humanize Text"):
    if text_input.strip():
        with st.spinner("Processing..."):
            prompt = f"""Your role is a "Text Humanizer".
Rewrite the following AI text in a more natural, human style.
Tone: {tone}.
Text: {text_input}
"""
            try:
                response = model.generate_content(prompt)
                st.success("✅ Humanized Text:")
                st.write(response.text)

                # Before/After comparison
                st.markdown("---")
                st.markdown("**Before:**")
                st.info(text_input)
                st.markdown("**After:**")
                st.success(response.text)

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("⚠️ Please enter some text first.")
