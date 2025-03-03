import streamlit as st
import urllib.parse

LOGOUT_URL = st.secrets["auth"]["logout_url"]

if not st.experimental_user.is_logged_in:
    st.login()
else:
    st.write(st.experimental_user)
    st.write(f"Hello, {st.experimental_user.name}!")

    if st.button("Log out"):
        st.logout()
        # Force browser to redirect to the Keycloak logout URL
        logout_redirect = urllib.parse.quote(LOGOUT_URL, safe="")
        st.markdown(f'<meta http-equiv="refresh" content="0;URL={LOGOUT_URL}">', unsafe_allow_html=True)