import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
from translator import translate_text

from language_config import LANGUAGES

st.set_page_config("TransLingua", layout="centered")
st.title("🌍 TransLingua – AI Language Translator")

text = st.text_area("Enter text to translate")
source = st.selectbox("Source Language", list(LANGUAGES.keys()))
target = st.selectbox("Target Language", list(LANGUAGES.keys()))

if st.button("Translate"):
    result = translate_text(text, source, target)
    st.success(result)
    
    from tts_utils import generate_audio
    audio_file = generate_audio(result, target)
    if audio_file:
        st.audio(audio_file, format='audio/mp3')
    else:
        st.warning("Audio not available for this language.")
