import streamlit as st
import time
def subheadingtext(text:str):
    message = []
    response = st.empty()
    tokens = list(text)
    for i in tokens:
        message.append(i)
        result = "".join(message)
        response.markdown(f'### {result} ',unsafe_allow_html=True)
        time.sleep(0.035)