
from translator import translate_text
import time

print("Starting translation test...")
start = time.time()
try:
    # Short text, fast translation
    text = "Hello"
    res = translate_text(text, "English", "French")
    print(f"Translation successful: {res}")
except Exception as e:
    print(f"Translation failed: {e}")
    # Print full traceback
    import traceback
    traceback.print_exc()

print(f"Finished in {time.time() - start:.2f}s")
