import streamlit as st
import time

def show():
    st.write("⚙️ Load Settings")
    # --- 8. PROGRESS BAR ---
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        progress_bar.progress(i + 1)
    st.success("Loading completed! ✅")

    # --- 9. STATUS MESSAGES ---
    if st.checkbox("Show success message"):
        st.success("✅ Everything is working perfectly!")

    # --- 10. MULTISELECT ---
    options = st.multiselect("Select your favorite colors:", ["Red", "Blue", "Green", "Yellow"], default=["Red"])
    st.write("You selected:", options)
