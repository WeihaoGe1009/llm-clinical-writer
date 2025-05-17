# 🧠 LLM-Powered Clinical Writer Assistant (WIP)

This project is a work-in-progress prototype of an interactive tool for generating structured clinical trial documents such as Protocols, Clinical Study Reports (CSRs), and Statistical Analysis Plans (SAPs) using large language models (e.g., LLaMA 3.8 via Hugging Face).

The goal is to allow users to:
- Select document type (protocol, CSR, SAP)
- Fill in structured input fields
- Generate outline or draft content using Markdown templates and optionally call an LLM

---

## 🚧 Status

✅ Features implemented so far:

🔜 Features planned:
- Streamlit interface with basic inputs
- Template loading and field substitution using Markdown
- LLM integration via Hugging Face (e.g., LLaMA, distilGPT2)
- Automatic fallback to CPU if no CUDA is available
- Outline vs full-draft toggle
- Editable output panel and export
- Hugging Face Spaces/Gradio demo
- More advanced prompt customization

---

## 📦 Setup (Local Only for Now)

Clone the repo and set up your environment:

```bash
git clone https://github.com/WeihaoGe1009/llm-clinical-writer.git
cd llm-clinical-writer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 💡 To Run the Streamlit App

After activating your virtual environment and installing dependencies, run:

```bash
streamlit run app.py
```
---

## 🔐 Hugging Face Access
If you're using gated models (e.g., Meta LLaMA 3), log in via CLI:

```bash
pip install huggingface_hub
huggingface-cli login
```

Or manually save your token in `~/.huggingface/token`.

## 📁 Structure

```bash
llm-clinical-writer/
├── app.py                  # Streamlit UI
├── generate.py             # Template + LLM logic
├── templates/              # Markdown templates 
├── examples/               # Sample inputs/outputs
├── requirements.txt
└── .progress_log/          # Dev notes 

```

