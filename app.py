# streamlit app.py
import streamlit as st

from learn import learn_page
from discovery import discovery_page
import streamlit_shadcn_ui as ui
from streamlit_extras.stylable_container import stylable_container
#from streamlit_option_menu import option_menu

from translation import translation_page

st.set_page_config(page_title="LANGUATOUR AI", page_icon="", layout="wide")

def inject_custom_css():
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


inject_custom_css()
value = ui.tabs(options=['DISCOVERY', 'TRANSLATION', 'LEARN'], default_value='DISCOVERY', key="kanaries")

with ui.card(key="image"):
    if value == "DISCOVERY":
       discovery_page()
    elif value == "TRANSLATION":
        translation_page() 
    elif value == "LEARN":
        learn_page()


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

