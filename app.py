import requests
import json
import time
import numpy as np 
import pandas as pd
import streamlit as st
from streamlit_lottie import st_lottie
from st_on_hover_tabs import on_hover_tabs

st.set_page_config('DASHBOARD',layout="wide")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)
#load lottie files
def load_lottie_file(filepath:str):
    with open(filepath,"r") as f:
        return json.load(f)
def subheadingtext(text:str):
    message = []
    response = st.empty()
    tokens = list(text)
    for i in tokens:
        message.append(i)
        result = "".join(message)
        response.markdown(f'### {result} ',unsafe_allow_html=True)
        time.sleep(0.035)
        # time.sleep(0.12)
# Hide the "Made with Streamlit" footer
# Define a CSS style for the text
hide_streamlit_style="""
    <style>
    #MainMenu{visibility:hidden;}
    footer{visibility:hidden;}
    h1 {
        color: #01FFB3 ;
    }
    h2 {
        color: darkorange;
    }
    h3 {
        color: red;
        # color: #12FFE2;
    }
    /* The progress bars */
        .stProgress > div > div > div > div {
            background: linear-gradient(to right, #00EEFF, #01FFB3);
            border-radius: 10px;
        }
        /* The text inside the progress bars */
        .stProgress > div > div > div > div > div {
            color: white;
        }
    </style>
    """
st.markdown(hide_streamlit_style,unsafe_allow_html=True)

lottie_file1 =load_lottie_file('./assets/GD.json')
lottie_file2 =load_lottie_file('./assets/GDSC.json')
lottie_file3 =load_lottie_file('./assets/GLoading.json')
with st.sidebar:
    st_lottie(lottie_file2,speed=0.5,reverse=False,height=100,width=260)
    tabs = on_hover_tabs(tabName=['Dashboard', 'GenAI', 'Cloud Foundations'], 
                         iconName=['bar_chart_4_bars', 'sports_esports', 'cloud'], default_choice=0)

if tabs =='Dashboard':
    c1,c2= st.columns([0.3,1.2])
    with c2:
        st.title(":blue[G]:green[D]:orange[S]:red[C]   :blue[M]:green[C]:orange[E]:red[T] GCSJ :orange[Dashboard] : :red[2023]",anchor=False)

    file= st.file_uploader("Upload The Results csv file",type='csv')
    if file != None:
        Df = pd.read_csv(file,index_col=None)
        st.dataframe(Df)
    st.divider()
    c3,c4= st.columns([0.5,1.2])
    with c4:
        st_lottie(lottie_file1,speed=0.5,reverse=False,height=110,width=350)

if tabs =='GenAI':
    c1,c2= st.columns([0.4,1.2])

    with c2:    
        st.title(":orange[Generative] :red[AI] Arcade :blue[Game]")
        subheadingtext(f"⚠️ Stay tuned! This event starts on {':orange[16 October]'}")
    c3,c4= st.columns([0.5,1.2])
    with c4:
        st_lottie(lottie_file3,speed=0.5,reverse=False,height=110,width=350)
if tabs =='Cloud Foundations':
    c1,c2= st.columns([0.2,1.2])
    with c2:
        st.title(":red[Google] :blue[Cloud] Computing :orange[Foundations]")
    st.divider()
    # Create an expandable section
    with st.expander("Click to toggle"):
        st.markdown("""
    ## 1. Cloud Computing Fundamentals :
    - ### Create and Manage Cloud Resources
    ## 2. Infrastructure in Google Cloud :
    - ### Perform Foundational Infrastructure Tasks in Google Cloud
    ## 3. Networking & Security in Google Cloud :
    - ### Build and Secure Networks in Google Cloud
    ## 4. Data, ML, and AI in Google Cloud :
    - ### Perform Foundational Data, ML, and AI Tasks in Google Cloud
    """)

        
    

