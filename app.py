# streamlit app.py

import streamlit as st
# from modules.translator import speech_to_speech, dub_radio_to_english
def main():
    # speech_to_speech()
    # Example usage:
    # api_key = "1358e1329e9c1d77c368d8ff1b7499ce"
    # radio_file_path = "D:/Git Hub Repos/AI-Verse/audio/Recording.m4a"
    # name = "Radio Dub"

    # source_url = "D:/Git Hub Repos/AI-Verse/audio/Recording.m4a"
    # dub_info = dub_radio_to_english(api_key, radio_file_path, name, source_url)
    # if dub_info:
    #     print("Dubbing created successfully!")
    
    st.write("""
        # AI Verse
        Your *tourism* and *cultural preservation* App
    """)
    st.sidebar.title("Side Bar title")

   
    
if __name__ == "__main__":
    main()
