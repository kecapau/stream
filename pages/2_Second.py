import streamlit as st
import time

i = 0
placeholder = st.empty()

while True:
    placeholder.title(f'counting: {i}')
    i += 1
    time.sleep(1)