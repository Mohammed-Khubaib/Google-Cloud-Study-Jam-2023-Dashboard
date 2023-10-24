# not part of app
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_elements import elements, mui, html
from streamlit_elements import nivo
import nivo_chart as nc
import random
import time
#trying Line
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
        "height": 300,
        "width": 900,
        "from": "2023-10-10",
        "to": "2023-10-30",
        "emptyColor": "gray",
        "colors": ["#61cdbb", "#97e3d5", "#e8c1a0", "#f47560"],
        "margin": {"top": 10, "right": 200, "bottom": 0, "left": 30},

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



DATA = [
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

TimeRange = {
    "data" : DATA ,
    "layout": {
        "title": "October 2023",
        "type": "calendar",
        # "height": 600,
        # "width": 700,
        "from": "2023-10-10",
        "to": "2023-10-30",
        "emptyColor": "gray",
        # "emptyColor":"#eeeeee",
        "colors": ["#61cdbb", "#97e3d5", "#e8c1a0", "#f47560"],
        # "margin": {"top": 10, "right": 200, "bottom": 0, "left": 30},
        "margin": {"top": 40, "right": 200, "bottom": 100, "left": 40},
        "monthLegendPosition":"before",
        "weekdayLegendOffset":75,
        "weekdayTicks":[1, 3, 5],
        "firstWeekday":'monday',
        "dayBorderWidth":2,
        "dayBorderColor":"#111",
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
                "translateX": -60,
                "translateY": -60,
                "symbolSize": 20
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
nc.nivo_chart(data=TimeRange["data"], layout=TimeRange["layout"], key="TimeRange")

def Theam(val):
    if val>1 and val<=20:
        st.write("""
        <style>
            /* The progress bars */
            .stProgress > div > div > div > div {
                background: linear-gradient(to right, red, orange);
                border-radius: 10px;
            }

            /* The text inside the progress bars */
            .stProgress > div > div > div > div > div {
                color: white;
            }
        </style>
        # """, unsafe_allow_html=True)
    elif val>20 and val<=30:
        st.write("""
        <style>
            /* The progress bars */
            .stProgress > div > div > div > div {
                background: linear-gradient(to right, orangered,yellow );
                border-radius: 10px;
            }
        </style>
        # """, unsafe_allow_html=True)
    elif val>20 and val<=40:
        st.write("""
        <style>
            /* The progress bars */
            .stProgress > div > div > div > div {
                background: linear-gradient(to right, lightgreen, green);
            }
        </style>
        # """, unsafe_allow_html=True)

# i=st.number_input("Enter the value of i",min_value=0,max_value=100,step=5,value=100)
progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(40):
    time.sleep(0.05)
    Theam(int(percent_complete))
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)