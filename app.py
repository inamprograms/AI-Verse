# streamlit app.py

import streamlit as st
from modules.translator import audio_to_text, text_to_audio, translate
def main():
    
    st.write("""
        # AI Verse
        Your *tourism* and *cultural preservation* App
    """)
    source_language = "ar"
    dummy = "أنا مهندس برمجيات أحب البرمجة"
    translate(source_language, dummy)
    # text = audio_to_text()
    # print("Text:", text)
    # text_to_audio(text)
    st.sidebar.title("Side Bar title")

   
    
if __name__ == "__main__":
    main()
