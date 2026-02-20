
import os
from dotenv import load_dotenv
from translator import translate_text

# Load env vars
load_dotenv()

# Test translation
text = "Hello world"
src = "English"
tgt = "French"

print(f"Testing translation: '{text}' from {src} to {tgt}")
try:
    result = translate_text(text, src, tgt)
    print(f"Result: {result}")
except Exception as e:
    print(f"Error: {e}")
