# app.py
import streamlit as st
from generate import generate_document

st.title("LLM-Powered Clinical Document Generator")

doc_type = st.selectbox("Choose document type:", ["protocol", "csr", "sap"])
use_llm = st.checkbox("Use LLM to expand content", value=False)

# Example input fields
inputs = {
    "study_title": st.text_input("Study Title", "A Phase II Study of AI-generated Protocols"),
    "primary_endpoint": st.text_input("Primary Endpoint", "Time to draft completion"),
    "study_design": st.text_input("Study Design", "Open-label, single-arm"),
    "population": st.text_input("Population", "Clinical document authors"),
    "intervention": st.text_input("Intervention", "Use of LLM writing assistant"),
}

if st.button("Generate"):
    output = generate_document(doc_type, inputs, use_llm=use_llm)
    st.text_area("Generated Document", value=output, height=400)
