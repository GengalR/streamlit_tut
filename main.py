import streamlit as st
import home
import data
import charts
import settings

# Check if User is Logged in
if not st.experimental_user.is_logged_in:
    st.login()
else:
    # --- 1. SIDEBAR MENU ---
    # Sidebar Navigation Menu
    menu = st.sidebar.radio("Navigation", ["Home", "Data", "Charts", "Settings"])

    # Show the Username in Sidebar
    st.sidebar.write(f"Logged in as: \t **{st.experimental_user.name}**")

    # Page Content
    st.write(f"Welcome to the **{menu}** Page!")

    if menu == "Home":
        home.show()
        st.write(st.experimental_user) # keycloak info

    elif menu == "Data":
        data.show()

    elif menu == "Charts":
        charts.show()

    elif menu == "Settings":
        settings.show()

    # Logout Button with Keycloak Redirect
    LOGOUT_URL = st.secrets["auth"]["logout_url"]
    if st.sidebar.button("🚪 Logout"):
        st.logout()
        st.markdown(f'<meta http-equiv="refresh" content="0;URL={LOGOUT_URL}">', unsafe_allow_html=True)
