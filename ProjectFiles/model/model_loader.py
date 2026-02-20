import os
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def load_model():
    model_name = "facebook/nllb-200-distilled-600M"
    token = os.getenv("HF_TOKEN")
    tokenizer = AutoTokenizer.from_pretrained(model_name, token=token)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name, token=token)
    return tokenizer, model
