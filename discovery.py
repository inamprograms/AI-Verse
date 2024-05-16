import streamlit_shadcn_ui as ui
import streamlit as st

def discovery_page(): 
    with ui.card(key="card2"):
        ui.element("button", key="card2_btn", text="Nest Submmit", variant="outline")
    with ui.card(key="card"):
        ui.element("button", key="card2_btn", text="Nest Submmit", variant="outline")
    with ui.card(key="card"):
        ui.element("button", key="card2_btn", text="Nest Submmit", variant="outline")
    with ui.card(key="card"):
        ui.element("button", key="card2_btn", text="Nest Submmit", variant="outline")