
from models.model_loader import load_model
from language_config import LANGUAGES

print("Loading model/tokenizer...")
tokenizer, _ = load_model()

print(f"Tokenizer class: {type(tokenizer)}")
print(f"Has 'lang_code_to_id': {hasattr(tokenizer, 'lang_code_to_id')}")

# Try alternative
tgt_code = "fra_Latn"
try:
    token_id = tokenizer.convert_tokens_to_ids(tgt_code)
    print(f"Token ID for '{tgt_code}' via convert_tokens_to_ids: {token_id}")
except Exception as e:
    print(f"Error via convert_tokens_to_ids: {e}")

# Check vocab size or special tokens
print(f"Vocab size: {tokenizer.vocab_size}")
