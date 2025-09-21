import streamlit as st

st.title("Demo Session State & Callback")

# init counter
if "counter" not in st.session_state:
    st.session_state.counter = 0

def increment():
    st.session_state.counter += 1

def reset():
    st.session_state.counter = 0

st.metric("Counter", st.session_state.counter)
st.button("\\+Increment", on_click=increment)
st.button("Reset", on_click=reset)

st.subheader("Form with Callback")
def form_callback():
    st.write(f"Slider value: {st.session_state.my_slider}")
    st.write(f"Checkbox: {st.session_state.my_checkbox}")

with st.form("my_form"):
    st.slider("My slider", 0, 10, 5, key="my_slider")
    st.checkbox("Yes or No", key="my_checkbox")
    st.form_submit_button("Submit", on_click=form_callback)
