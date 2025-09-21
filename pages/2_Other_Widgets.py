import streamlit as st
import time

st.title("Demo Status Widgets")

# Spinner
with st.spinner("Loading for 2 seconds..."):
    time.sleep(2)
st.success("Done!")

# Status messages
st.info("ℹ️ This is an info message.")
st.success("✅ This is a success message.")
st.warning("⚠️ This is a warning message.")
st.error("❌ This is an error message.")

# Toast notification
if st.button("Show Toast"):
    st.toast("This is a toast notification!", icon="🎉")
