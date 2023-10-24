from streamlit_gsheets import GSheetsConnection
import streamlit as st
def File():
    url = "https://docs.google.com/spreadsheets/d/1OQEZzqf0tl5xrRAg0QQkBwI3ylXNlrAqIG5cMmD8VyE/edit#gid=0"
    # url = "https://docs.google.com/spreadsheets/d/1OQEZzqf0tl5xrRAg0QQkBwI3ylXNlrAqIG5cMmD8VyE/edit?usp=sharing"
    conn = st.experimental_connection("gsheets", type=GSheetsConnection)
    file = conn.read(spreadsheet=url, usecols=[0, 1,2,3,4,5,6,7,8,9,10])
    return file