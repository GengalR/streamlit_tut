import streamlit as st
import pandas as pd

def show():
    # --- 5. FILE UPLOAD ---
    uploaded_file = st.file_uploader("Upload a Excel file", type=["xlsx, xls"])
    if uploaded_file:
        df_uploaded = pd.read_excel(uploaded_file)
        st.write("Uploaded Data:")
    else:
        df_uploaded = pd.read_excel("data/test_data.xlsx")

    st.write(f"Loaded Data: {uploaded_file}")

    # filter columns
    relevant_cols = st.multiselect("Select columns", df_uploaded.columns.tolist())
    if relevant_cols:
        df_uploaded = df_uploaded[relevant_cols]
    st.dataframe(df_uploaded)

    # --- 6. EXPANDER ---
    with st.expander("Get detailed info"):
        st.dataframe(df_uploaded.describe())
