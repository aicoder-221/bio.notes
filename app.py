import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="Biology Chapter 1", layout="wide")

st.title("📘 Biology Chapter 1 - Interactive Notes")

# Try possible file names
file_candidates = ["bio.ch.1.html", "bio.ch.1"]

html_content = None

for file in file_candidates:
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            html_content = f.read()
        break

if html_content:
    components.html(html_content, height=800, scrolling=True)
else:
    st.error("HTML file not found. Make sure 'bio.ch.1.html' (or 'bio.ch.1') is in the repo.")
