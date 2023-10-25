from streamlit_elements import nivo
from streamlit_elements import elements, mui
def pieChart(tab,yes_count,no_count) :
    with elements(str(tab)):
                DATA = [
                    {"id": "Yes", "label": "Yes", "value": int(yes_count),"color": "hsl(21, 70%, 50%)"},
                    {"id": "No", "label": "No", "value": int(no_count), "color": "hsl(0, 70%, 50%)"}
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
                            'from' : DATA,
                            'modifiers': 'darker'
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
                                10
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
                                    "symbolSize": 14,
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
                            "background": "#0e1016",
                            "textColor": "#fff",
                            "tooltip": {
                                "container": {
                                    "background": "#111",
                                    "color": "#fff",
                                }
                            }
                        }
                    )



def pieChart4(tab,completed_status) :
    with elements(str(tab)):
                DATA = [
                    {"id": "0/4", "label": "0", "value": int(completed_status[0]),"color": "hsl(21, 70%, 50%)"},
                    {"id": "1/4", "label": "1", "value": int(completed_status[1]), "color": "hsl(0, 70%, 50%)"},
                    {"id": "2/4", "label": "2", "value": int(completed_status[2]),"color": "hsl(21, 70%, 50%)"},
                    {"id": "3/4", "label": "3", "value": int(completed_status[3]), "color": "hsl(0, 70%, 50%)"},
                    {"id": "4/4", "label": "4", "value": int(completed_status[4]), "color": "hsl(0, 70%, 50%)"},
                ]
                with mui.Box(sx={"height": 400}):
                    nivo.Pie(
                        data= DATA,
                        keys=["0","1","2","3","4"],
                        margin={ "top": 40, "right": 80, "bottom": 80, "left": 80 },
                        innerRadius=0.5,
                        padAngle=0.7,
                        cornerRadius=3,
                        activeOuterRadiusOffset=8,
                        borderWidth=1,
                        borderColor = {
                            'from' : DATA,
                            "modifiers": 'brighter'
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
                                1000
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
                                "id": "0/4"
                            },
                            "id": "dots"
                        },
                        {
                            "match": {
                                "id": "1/4"
                            },
                            "id": "lines"
                        },
                        {
                            "match": {
                                "id": "2/4"
                            },
                            "id": "lines"
                        },
                        {
                            "match": {
                                "id": "3/4"
                            },
                            "id": "dots"
                        },
                        {
                            "match": {
                                "id": "4/4"
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
                                    "itemWidth": 50,
                                    "itemHeight": 18,
                                    "itemTextColor": '#999',
                                    "itemDirection": 'left-to-right',
                                    "itemOpacity": 2,
                                    "symbolSize": 14,
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
                            "background": "#0e1016",
                            "textColor": "#fff",
                            "tooltip": {
                                "container": {
                                    "background": "#111",
                                    "color": "#fff",
                                }
                            }
                        }
                    )


def pieChart9(tab,completed_status) :
    with elements(str(tab)):
                DATA = [
                    {"id": "0", "label": "0", "value": int(completed_status[0]),"color": "hsl(21, 70%, 50%)"},
                    {"id": "1", "label": "1", "value": int(completed_status[1]), "color": "hsl(0, 70%, 50%)"}
                ]
                with mui.Box(sx={"height": 400}):
                    nivo.Pie(
                        data= DATA,
                        keys=["0","1","2","3","4","5","6","7","8","9"],
                        margin={ "top": 40, "right": 80, "bottom": 80, "left": 80 },
                        innerRadius=0.5,
                        padAngle=0.7,
                        cornerRadius=3,
                        colors={ 'scheme': 'nivo' },
                        activeOuterRadiusOffset=8,
                        borderWidth=2,
                        borderColor = {
                            'from' : "DATA",
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
                                1000
                            ]
                        ]
                        },
                        defs = [
                        {
                            "id": "dots",
                            "type": "patternDots",
                            "background": "inherit",
                            "color": "#FFFFFF4D",
                            "size": 5,
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
                                "id": "0"
                            },
                            "id": "dots"
                        },
                        {
                            "match": {
                                "id": "1"
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
                                    "itemWidth": 40,
                                    "itemHeight": 18,
                                    "itemTextColor": '#999',
                                    "itemDirection": 'left-to-right',
                                    "itemOpacity": 2,
                                    "symbolSize": 14,
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
                            "background": "#0e1016",
                            "textColor": "#fff",
                            "tooltip": {
                                "container": {
                                    "background": "#111",
                                    "color": "#fff",
                                }
                            }
                        }
                    )