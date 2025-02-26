import streamlit as st

# --- 1. APP TITLE & DESCRIPTION ---
st.title("📌 Streamlit Basics Tutorial")
st.write("Welcome to this Streamlit tutorial! Here, you'll learn the most important features.")

# --- 2. TEXT INPUT & DISPLAYING DATA ---
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, **{name}**! 👋")

# write code block
code_block = """
    def greeting():
        return "Hello"
    """

# --- 3. BUTTON ---
if st.button("Click me!"):
    st.success("🎉 Button clicked!")
