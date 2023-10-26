
from streamlit_elements import elements, mui, html
from streamlit_elements import nivo
import nivo_chart as nc

def LineChart():
    with elements("Study_Jam"):
        DATA = [
            {
                "id": "Study Jam Finishers",
                "color": "hsl(191, 70%, 50%)",
                # "color": "hsl(320, 70%, 50%)",
                "data": [
                    {"x": 4, "y": 0},
                    {"x": 5, "y": 0},
                    {"x": 6, "y": 0},
                    {"x": 7, "y": 0},
                    {"x": 8, "y": 0},
                    {"x": 9, "y": 0},
                    {"x": 10, "y": 0},
                    {"x": 11, "y": 0},
                    {"x": 12, "y": 0},
                    {"x": 13, "y": 0},
                    {"x": 14, "y": 1},
                    {"x": 15, "y": 1},
                    {"x": 16, "y": 1},
                    {"x": 17, "y": 3},
                    {"x": 18, "y": 9},
                    {"x": 19, "y": 16},
                    {"x": 20, "y": 19},
                    {"x": 21, "y": 21},
                    {"x": 22, "y": 23},
                    {"x": 23, "y": 23},
                    {"x": 24, "y": 28},
                    {"x": 25, "y": 36},
                    {"x": 26, "y": 43},
                ]
            
            }
        ]
        with mui.Box(sx={"height": 500}):
            nivo.Line(
                data=DATA,
                margin={ "top": 50, "right": 110, "bottom": 100, "left": 60 },
                xScale={ "type": "point" },
                yScale={
                    "type": "linear",
                    "min": "auto",
                    "max": "auto",
                    "stacked": True,
                    "reverse": False
                },
                # yFormat=">-.2f",
                axisTop= None,
                axisRight= None,
                axisBottom={
                    "tickSize": 11,
                    "tickPadding": 15,
                    "tickRotation": 0,
                    "legend": 'October',
                    "legendOffset": 56,
                    "legendPosition": 'middle'
                },
                axisLeft={
                    "tickSize": 11,
                    "tickPadding": 13,
                    "tickRotation": 15,
                    "legend": "Completionists",
                    "legendOffset": -54,
                    "legendPosition": "middle"
                },
                enableGridX=False,
                enableGridY=False,
                # enableSlices="y",
                colors={ 'scheme': 'accent' },
                enablePointLabel=True,
                pointLabel="y",
                pointLabelYOffset=24,
                lineWidth=6,
                pointSize=15,
                pointColor={ "theme": "background" },
                pointBorderWidth=5,
                pointBorderColor={ "from": "serieColor" },
                # pointLabelYOffset=-12,
                enableArea=True,
                useMesh=True,
                legends=[
                    {
                        "anchor": "bottom-left",
                        "direction": "column",
                        "justify": False,
                        "translateX": 110,
                        "translateY": 60,
                        "itemsSpacing": 0,
                        "itemDirection": "left-to-right",
                        "itemWidth": 100,
                        "itemHeight": 20,
                        "itemOpacity": 0.75,
                        "symbolSize": 20,
                        'symbolShape': "circle",
                        "symbolBorderColor": "rgba(0, 0, 0, .5)",
                        "effects": [
                            {
                                "on": 'hover',
                                "style": {
                                    "itemBackground": "#0e1016",
                                    "itemOpacity": 1
                                }
                            }
                        ]
                    }
                ],
                theme={
                    "background": "#0e1016",
                    "textColor": "#fff",
                    "tooltip": {
                        "container": {
                            "background": "#0e1016",
                            "color": "#fff",
                        }
                    }
                }

                )