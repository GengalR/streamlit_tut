import streamlit as st
import home
import data
import charts
import settings

# --- 1. SIDEBAR MENU ---
menu = st.sidebar.radio("Navigation", ["Home", "Data", "Charts", "Settings"])

if menu == "Home":
    home.show()

elif menu == "Data":
    data.show()

elif menu == "Charts":
    charts.show()

elif menu == "Settings":
    settings.show()