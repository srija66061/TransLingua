from models.model_loader import load_model
from language_config import LANGUAGES

tokenizer, model = load_model()

def translate_text(text, src, tgt):
    src_code = LANGUAGES.get(src, "eng_Latn")
    tgt_code = LANGUAGES.get(tgt, "eng_Latn")
    
    tokenizer.src_lang = src_code
    inputs = tokenizer(text, return_tensors="pt")
    
    translated_tokens = model.generate(
        **inputs, 
        forced_bos_token_id=tokenizer.convert_tokens_to_ids(tgt_code)
    )
    return tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
