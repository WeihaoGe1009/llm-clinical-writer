import os
from pathlib import Path
import torch
from huggingface_hub import login
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline


# Load Hugging Face Token (optional safety check)
def get_token():
    token_file = Path.home() / ".huggingface" / "token"
    return token_file.read_text().strip() if token_file.exists() else None


# Load a markdown template from the /templates directory
def load_template(doc_type: str) -> str:
    template_path = Path("templates") / f"{doc_type.lower()}_template.md"
    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")
    return template_path.read_text()


# Fill placeholders in the template using a dictionary
def fill_template(template: str, inputs: dict) -> str:
    for key, value in inputs.items():
        template = template.replace(f"{{{{{key}}}}}", value)
    return template


# Send prompt to LLM and return generated output
def generate_from_llm(prompt: str, model_id: str = "meta-llama/Meta-Llama-3-8B-Instruct") -> str:
    token = get_token()
    if not token:
        raise RuntimeError("No Hugging Face token found. Login required.")

    use_cuda = torch.cuda.is_available()

    if not use_cuda:
        print("🔧 CUDA not available — loading model on CPU")
        tokenizer = AutoTokenizer.from_pretrained(model_id, use_auth_token=True)
        model = AutoModelForCausalLM.from_pretrained(model_id, use_auth_token=True)
        generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=-1)
    else:
        print("⚡ CUDA is available — using Accelerate with GPU")
        tokenizer = AutoTokenizer.from_pretrained(model_id, use_auth_token=True)
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            device_map="auto",
            torch_dtype="auto",
            use_auth_token=True,
        )
        generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

    result = generator(prompt, max_new_tokens=512, do_sample=True, temperature=0.7)

    return result[0]["generated_text"]


# Master function
def generate_document(doc_type: str, inputs: dict, use_llm: bool = False) -> str:
    template = load_template(doc_type)
    filled = fill_template(template, inputs)

    if use_llm:
        return generate_from_llm(filled)
    else:
        return filled