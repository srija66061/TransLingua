
from gtts import gTTS
import io

# Map NLLB/App language names to gTTS language codes
GTTS_LANG_MAP = {
    "English": "en",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Spanish": "es",
    "Tamil": "ta",
    "Telugu": "te"
}

def generate_audio(text, language_name):
    """
    Generates audio from text for the specified language.
    Returns: BytesIO object containing the audio data.
    """
    if not text:
        return None
    
    lang_code = GTTS_LANG_MAP.get(language_name, "en")
    
    try:
        tts = gTTS(text=text, lang=lang_code)
        audio_fp = io.BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        return audio_fp
    except Exception as e:
        print(f"TTS Error: {e}")
        return None
