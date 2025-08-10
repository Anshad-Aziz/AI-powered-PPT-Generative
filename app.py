import streamlit as st
from ppt_creator import create_ppt
from llm_content import generate_presentation_content
from pexels_api import get_image_url

st.set_page_config(page_title="AI PPT Generator", layout="wide")

# ChatGPT dark style
st.markdown("""
    <style>
    body {background-color: #343541; color: white;}
    .stTextInput > div > div > input {background-color: #40414f; color: white;}
    </style>
""", unsafe_allow_html=True)

st.title("📊 AI Powered PPTX Generator")
topic = st.text_input("Enter your topic:")

if st.button("Generate PPT"):
    with st.spinner("Generating presentation..."):
        content = generate_presentation_content(topic)
        if not content:
            st.error("Failed to generate content.")
        else:
            ppt = create_ppt(content, get_image_url)
            file_path = f"{topic.replace(' ','_')}.pptx"
            ppt.save(file_path)
            st.success("PPT generated successfully!")
            with open(file_path, "rb") as f:
                st.download_button("Download PPT", f, file_name=file_path)
