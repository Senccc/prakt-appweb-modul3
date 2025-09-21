import streamlit as st
import time

st.title("Demo Caching")

st.write("Caching memperbolehkan kita untuk menggunakan kembali hasil fungsi daripada menghitung ulang.")

@st.cache_data
def slow_square(x):
    time.sleep(2)  # simulate slow work
    return x * x

num = st.number_input("Masukkan angka:", value=5)
if st.button("Hitung Kuadrat"):
    result = slow_square(num)
    st.success(f"Result: {result}")
    st.info("Re-run dengan nilai yang sama akan instan berkat caching")
