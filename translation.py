import streamlit_shadcn_ui as ui
import streamlit as st
from audio_recorder_streamlit import audio_recorder


def translation_page():
    choice = ui.select(options=["fongbe", "dindi", "yoruba"])
    st.markdown(f"Currrent value: {choice}")
    audio_bytes = audio_recorder(
        text="",
        recording_color="#e8b62c",
        neutral_color="#6aa36f",
        icon_name="microphone",
        icon_size="6x",
    )
    if audio_bytes:
        st.audio(audio_bytes, format="audio/wav")
    st.image('pulse.png', width=350)
    st.divider()
    ui.button(text="Translate", key="styled_btn_tailwind5", className="bg-green-500 text-white")
    st.audio("tech.mp3", format="audio")

    