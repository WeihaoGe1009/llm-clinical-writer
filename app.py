# app.py
import streamlit as st
from generate import generate_document

import json
from utils import excel_to_json
from generate import generate_trial_design


# the basic toy example
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



# generate clinical trial section by section

### General Information - Title, sponsor, registraition info

### Introduction & Background - Scientific rationale
#### requires expertise and is prone to hallucination for citation
#### best way is to have user-provide, but maybe AI can help with improviement

### Objectives & Endpoints - provided by user
#### can be used as extra prompt in other parts of the document

### Trial Design 

st.header("Generate Trial Design Section")

# File upload
uploaded_file = st.file_uploader("Upload Excel or JSON", type=["xlsx", "json"])
input_data = {}

if uploaded_file:
    if uploaded_file.name.endswith(".xlsx"):
        input_data = excel_to_json(uploaded_file)
    elif uploaded_file.name.endswith(".json"):
        input_data = json.load(uploaded_file)

# Manual fallback
with st.expander("Or fill manually"):
    design = st.text_input("Study Design")
    arms = st.text_input("Number of Arms")
    allocation = st.text_input("Allocation Ratio")
    blinding = st.text_input("Blinding")
    duration = st.text_input("Study Duration")
    other = st.text_area("Other Notes (optional)")

    if st.button("Generate from Manual Input"):
        input_data = {
            "design": design,
            "arms": arms,
            "allocation": allocation,
            "blinding": blinding,
            "duration": duration,
            "extras": {"other_notes": other} if other else {}
        }

# Show result
if input_data:
    with st.spinner("Generating section..."):
        section_text = generate_trial_design(input_data)
        st.markdown("### 📄 Trial Design Section")
        st.code(section_text, language="markdown")


### Selection of Study Participants
#### user will write them because this is less effort than inputting them into this app.
#### maybe we can use this as prompt to help with other parts

### interventions - templated

### safety & Efficacy Assessements - data collected, take in "endpoints" as prompt

### Ethical & Regulatory - informed consent, IRB - institutional defaults can be reused
#### not intended to store anything, still want to keep everything open-source 

### Data Handling and Monitoring - eCRF, audit trail, DMC - semi-templated
#### might be abit complicated with llm?
