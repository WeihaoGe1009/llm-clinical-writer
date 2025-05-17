import sys
import os
import transformers
import streamlit
from huggingface_hub import whoami

print("✅ Python path:", sys.executable)
print("✅ Environment active:", sys.prefix)
print("✅ Transformers version:", transformers.__version__)
print("✅ Streamlit version:", streamlit.__version__)
print("✅ Hugging Face login:", whoami())
