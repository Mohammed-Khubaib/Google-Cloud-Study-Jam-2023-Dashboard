import requests
import json
import time
import numpy as np 
import pandas as pd
import streamlit as st
from streamlit_lottie import st_lottie
from st_on_hover_tabs import on_hover_tabs
from streamlit_elements import nivo
from streamlit_elements import elements, mui, html
import nivo_chart as nc

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
    tabs = on_hover_tabs(tabName=['Dashboard','Cloud Foundations','GenAI'], 
                         iconName=['bar_chart_4_bars',  'cloud','sports_esports'], default_choice=0,
                         styles = {'navtab': {'background-color':'#272731',
                                                  'color': '#818181',
                                                  'font-size': '18px',
                                                  'transition': '.3s',
                                                  'white-space': 'nowrap',
                                                  'text-transform': 'uppercase'},
                                    'tabOptionsStyle': {':hover :hover': {'color': 'red',
                                                                      'cursor': 'pointer'}},              
                                                  
                                                  },
                        
                         )
# 'color': '#818181',
if tabs =='Dashboard':
    c1,c2= st.columns([0.3,1.2])
    with c2:
        st.title(":blue[G]:green[D]:orange[S]:red[C]   :blue[M]:green[C]:orange[E]:red[T] GCSJ :orange[Dashboard] : :red[2023]",anchor=False)

    file= st.file_uploader("Upload The Results csv file",type='csv')
    st.divider()
    tab1,tab2,tab3,tab4 = st.tabs(['Week 1','Week 2','Week 3','$$\color{orange}\sqrt{2}$$'])
    with tab1:
        if file != None:
            st.header("Week 1")
            Df = pd.read_csv(file,index_col=None)
            st.warning(Df.columns)
            st.dataframe(Df[['Student Name','Redemption Status','# of Courses Completed', '# of Skill Badges Completed', '# of GenAI Game Completed', 'Total Completions of both Pathways']])
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

    




with elements("nivo_pie"):
    DATA = [
        {"id": "lisp", "label": "lisp", "value": 223, "color": "hsl(21, 70%, 50%)"},
        {"id": "python", "label": "python", "value": 581, "color": "hsl(338, 70%, 50%)"},
        {"id": "c", "label": "c", "value": 561, "color": "hsl(50, 70%, 50%)"},
        {"id": "elixir", "label": "elixir", "value": 372, "color": "hsl(186, 70%, 50%)"},
        {"id": "make", "label": "make", "value": 377, "color": "hsl(93, 70%, 50%)"}
    ]
    with mui.Box(sx={"height": 600}):
        nivo.Pie(
            data= DATA,
            keys=[ "lisp", "python", "c","ruby","elixir","make" ],
            margin={ "top": 40, "right": 80, "bottom": 80, "left": 80 },
            innerRadius=0.5,
            padAngle=0.7,
            cornerRadius=3,
            activeOuterRadiusOffset=8,
            borderWidth=1,
            borderColor = {
                "from": "color",
                "modifiers": [
                    [
                        "darker",
                        0.2
                    ]
                ]
            },
            arcLinkLabelsSkipAngle=10,
            arcLinkLabelsTextColor="#fff",
            arcLinkLabelsThickness=5,
            arcLinkLabelsColor={ "from": 'color' },
            arcLabelsSkipAngle=2,
            arcLabelsTextColor={
            "from": 'color',
            "modifiers": [
                [
                    'darker',
                    2
                ]
            ]
            },
            defs = [
            {
                "id": "dots",
                "type": "patternDots",
                "background": "inherit",
                "color": "#FFFFFF4D",
                "size": 4,
                "padding": 2,
                "stagger": "true"
            },
            {
                "id": "lines",
                "type": "patternLines",
                "background": "inherit",
                "color": "rgba(255, 255, 255, 0.3)",
                "rotation": -45,
                "lineWidth": 6,
                "spacing": 10
            }
            ],

        fill = [
            {
                "match": {
                    "id": "lisp"
                },
                "id": "dots"
            },
            {
                "match": {
                    "id": "rust"
                },
                "id": "dots"
            },
            {
                "match": {
                    "id": "c"
                },
                "id": "dots"
            },
            {
                "match": {
                    "id": "python"
                },
                "id": "dots"
            },
            {
                "match": {
                    "id": "scala"
                },
                "id": "lines"
            },
            {
                "match": {
                    "id": "make"
                },
                "id": "lines"
            },
            {
                "match": {
                    "id": "elixir"
                },
                "id": "lines"
            },
            {
                "match": {
                    "id": "javascript"
                },
                "id": "lines"
            }
        ],
        legends=[
                    {
                        "anchor": 'bottom',
                        "direction": 'row',
                        # "justify": "false",
                        "translateX": 1,
                        "translateY": 76,
                        "itemsSpacing": 10,
                        "itemWidth": 100,
                        "itemHeight": 18,
                        "itemTextColor": '#999',
                        "itemDirection": 'left-to-right',
                        "itemOpacity": 2,
                        "symbolSize": 10,
                        "symbolShape": 'circle',
                        "effects": [
                            {
                                "on": 'hover',
                                "style": {
                                    "itemTextColor": '#fff'
                                }
                            }
                        ]
                    }
                ],
                theme={
                "background": "#111",
                "textColor": "#fff",
                "tooltip": {
                    "container": {
                        "background": "#111",
                        "color": "#fff",
                    }
                }
                }
        )




#trying Line
with elements("nivo_line"):
    DATA = [
        {
            "id": "japan",
            "color": "hsl(191, 70%, 50%)",
            "data": [
                {"x": "plane", "y": 114},
                {"x": "helicopter", "y": 76},
                {"x": "boat", "y": 205},
                {"x": "train", "y": 170},
                {"x": "subway", "y": 243},
                {"x": "bus", "y": 102},
                {"x": "car", "y": 56},
                {"x": "moto", "y": 186},
                {"x": "bicycle", "y": 15},
                {"x": "horse", "y": 261},
                {"x": "skateboard", "y": 181},
                {"x": "others", "y": 165},
            ]
        },
        {
            "id": "france",
            "color": "hsl(320, 70%, 50%)",
            "data": [
                {"x": "plane", "y": 35},
                {"x": "helicopter", "y": 197},
                {"x": "boat", "y": 128},
                {"x": "train", "y": 219},
                {"x": "subway", "y": 78},
                {"x": "bus", "y": 57},
                {"x": "car", "y": 170},
                {"x": "moto", "y": 278},
                {"x": "bicycle", "y": 4},
                {"x": "horse", "y": 271},
                {"x": "skateboard", "y": 146},
                {"x": "others", "y": 155},
            ]
        },
        {
            "id": "us",
            "color": "hsl(195, 70%, 50%)",
            "data": [
                {"x": "plane", "y": 69},
                {"x": "helicopter", "y": 84},
                {"x": "boat", "y": 64},
                {"x": "train", "y": 73},
                {"x": "subway", "y": 125},
                {"x": "bus", "y": 73},
                {"x": "car", "y": 41},
                {"x": "moto", "y": 244},
                {"x": "bicycle", "y": 148},
                {"x": "horse", "y": 12},
                {"x": "skateboard", "y": 279},
                {"x": "others", "y": 152},
            ]
        },
        {
            "id": "germany",
            "color": "hsl(312, 70%, 50%)",
            "data": [
                {"x": "plane", "y": 116},
                {"x": "helicopter", "y": 120},
                {"x": "boat", "y": 80},
                {"x": "train", "y": 229},
                {"x": "subway", "y": 229},
                {"x": "bus", "y": 126},
                {"x": "car", "y": 28},
                {"x": "moto", "y": 60},
                {"x": "bicycle", "y": 98},
                {"x": "horse", "y": 234},
                {"x": "skateboard", "y": 244},
                {"x": "others", "y": 232},
            ]
        },
        {
            "id": "norway",
            "color": "hsl(106, 70%, 50%)",
            "data": [
                {"x": "plane", "y": 225},
                {"x": "helicopter", "y": 205},
                {"x": "boat", "y": 1},
                {"x": "train", "y": 96},
                {"x": "subway", "y": 157},
                {"x": "bus", "y": 285},
                {"x": "car", "y": 200},
                {"x": "moto", "y": 33},
                {"x": "bicycle", "y": 68},
                {"x": "horse", "y": 285},
                {"x": "skateboard", "y": 174},
                {"x": "others", "y": 57},
            ]
        }
    ]
    with mui.Box(sx={"height": 500}):
        nivo.Line(
            data=DATA,
            margin={ "top": 50, "right": 110, "bottom": 50, "left": 60 },
            xScale={ "type": "point" },
            yScale={
                "type": "linear",
                "min": "auto",
                "max": "auto",
                "stacked": True,
                "reverse": False
            },
            yFormat=">-.2f",
            axisTop= None,
            axisRight= None,
            axisBottom={
                "tickSize": 5,
                "tickPadding": 5,
                "tickRotation": 0,
                "legend": 'transportation',
                "legendOffset": 36,
                "legendPosition": 'middle'
            },
            axisLeft={
                "tickSize": 5,
                "tickPadding": 5,
                "tickRotation": 0,
                "legend": "count",
                "legendOffset": -40,
                "legendPosition": "middle"
            },
            pointSize=10,
            pointColor={ "theme": "background" },
            pointBorderWidth=4,
            pointBorderColor={ "from": "serieColor" },
            pointLabelYOffset=-12,
            useMesh=True,
            legends=[
                {
                    "anchor": "bottom-right",
                    "direction": "column",
                    "justify": False,
                    "translateX": 100,
                    "translateY": 0,
                    "itemsSpacing": 0,
                    "itemDirection": "left-to-right",
                    "itemWidth": 80,
                    "itemHeight": 20,
                    "itemOpacity": 0.75,
                    "symbolSize": 12,
                    'symbolShape': "circle",
                    "symbolBorderColor": "rgba(0, 0, 0, .5)",
                    "effects": [
                        {
                            "on": 'hover',
                            "style": {
                                "itemBackground": "#111",
                                "itemOpacity": 1
                            }
                        }
                    ]
                }
            ],
            theme={
                "background": "#111",
                "textColor": "#fff",
                "tooltip": {
                    "container": {
                        "background": "#111",
                        "color": "#fff",
                    }
                }
            }

            )

DATA =[
        {"value": 1,"day": "2023-10-10"},
        {"value": 2,"day": "2023-10-11"},
        {"value": 3,"day": "2023-10-12"},
        {"value": 4,"day": "2023-10-13"},
        {"value": 5,"day": "2023-10-14"},
        {"value": 1,"day": "2023-10-15"},
        {"value": 2,"day": "2023-10-16"},
        {"value": 3,"day": "2023-10-17"},
        {"value": 4,"day": "2023-10-18"},
        {"value": 5,"day": "2023-10-19"},
        {"value": 1,"day": "2023-10-20"},
        {"value": 2,"day": "2023-10-21"},
        {"value": 3,"day": "2023-10-22"},
        {"value": 4,"day": "2023-10-23"},
        {"value": 5,"day": "2023-10-24"},
        {"value": 1,"day": "2023-10-24"},
        {"value": 2,"day": "2023-10-26"},
        {"value": 3,"day": "2023-10-27"},
        {"value": 4,"day": "2023-10-28"},
        {"value": 5,"day": "2023-10-29"},
        {"value": 1,"day": "2023-10-30"},
        {"value": 2,"day": "2023-10-31"},
        ]
st.markdown("$$\color{orange}\text{Calendar 2023} ")
st.latex(r'''x{\times}y''')
st.latex(r'''\color{darkorange}\cfrac{x}{y}  \frac{x}{y}''')
calendar_chart = {

   "data" : DATA ,
    "layout": {
        "title": "Calendar 2023",
        "type": "calendar",
        "height": 500,
        "width": 1200,
        "from": "2023-10-10",
        "to": "2023-10-30",
        "emptyColor": "gray",
        "colors": ["#61cdbb", "#97e3d5", "#e8c1a0", "#f47560"],
        "margin": {"top": 40, "right": 40, "bottom": 40, "left": 40},

        "yearSpacing": 40,
        "monthBorderColor": "#111",
        "dayBorderWidth": 2,
        "dayBorderColor": "#111",
        "legends": [
            {
                "anchor": "bottom-right",
                "direction": "row",
                "translateY": 36,
                "itemCount": 4,
                "itemWidth": 42,
                "itemHeight": 36,
                "itemsSpacing": 14,
                "itemDirection": "right-to-left",
            }
        ],
        "theme":{
            "background": "#111",
            "textColor": "#fff",
            "tooltip": {
                "container": {
                    "background": "#111",
                    "color": "#fff",
                }
            }
        }
    }
}
nc.nivo_chart(data=calendar_chart["data"], layout=calendar_chart["layout"], key="calendar_chart")
