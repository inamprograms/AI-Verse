import streamlit_shadcn_ui as ui
import streamlit as st

def learn_page():
    col1, col2 = st.columns([1, 2], gap="medium")
    with col1:
        st.image('beg.png', width=78)

    with col2:
        st.title("BEGINNERS")
        st.markdown("Expression of the usual vocabulary")
        ui.button(text="GO", key="styled_btn_tailwind", className="bg-green-500 text-white")
        
    col1, col2 = st.columns([1, 2], gap="medium")
    with col1:
        st.image('beg.png', width=78)

    with col2:
        st.title("CONVERSATION")
        st.markdown("Expression of the usual vocabulary")
        ui.button(text="GO", key="styled_btn_tailwind1", className="bg-green-500 text-white")
        
    col1, col2 = st.columns([1, 2], gap="medium")
    with col1:
        st.image('beg.png', width=78)

    with col2:
        st.title("DICTIONARIES")
        st.markdown("Expression of the usual vocabulary")
        ui.button(text="GO", key="styled_btn_tailwind2", className="bg-green-500 text-white", )
