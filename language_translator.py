# language_translator_app.py

import streamlit as st
from deep_translator import GoogleTranslator

# App title
st.title("Language Translator")

# Input from user
text = st.text_area("Enter text to translate:")

# Language options (GoogleTranslator supports 100+)
languages = ['english', 'french', 'hindi', 'telugu', 'spanish', 'german', 'chinese', 'japanese','hy']

# Language selectors
source_lang = st.selectbox("Source Language", languages, index=0)
target_lang = st.selectbox("Target Language", languages, index=1)

# Translate button
if st.button("Translate"):
    if source_lang == target_lang:
        st.warning("Source and target languages are the same.")
    elif not text.strip():
        st.warning("Please enter some text.")
    else:
        try:
            translation = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
            st.success(f"Translated Text:\n\n{translation}")
        except Exception as e:
            st.error(f"Translation failed: {e}")
