import streamlit as st

st.set_page_config(page_title="Biology Unit 1 Notes", layout="wide")

def load_html(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return f.read()

html = load_html("bio_unit1.html")

st.components.v1.html(html, height=1200, scrolling=True)
