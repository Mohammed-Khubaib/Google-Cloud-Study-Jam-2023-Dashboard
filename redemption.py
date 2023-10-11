import streamlit as st
import pandas as pd
import numpy as np
from streamlit_elements import elements, mui
from streamlit_elements import nivo
st.latex(r'''\color{red}\text{Redemtion Status}''')
with elements("nivo_pie"):
    DATA = [
        {"id": "Yes", "label": "Yes", "value": 377,"color": "hsl(120, 70%, 50%)"},
        {"id": "No", "label": "No", "value": 581, "color": "hsl(0, 70%, 50%)"}
    ]
    with mui.Box(sx={"height": 400}):
        nivo.Pie(
            data= DATA,
            keys=["Yes","No"],
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
                    "id": "Yes"
                },
                "id": "dots"
            },
            {
                "match": {
                    "id": "No"
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